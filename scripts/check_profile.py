"""Check that profile project claims have a dated source and links still exist."""

import argparse
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

PROJECT = re.compile(r"^### .*?\[([^\]]+)\]\(https://github\.com/XIAOXUsop/[^)]+\)", re.M)
PROVENANCE = re.compile(r"验证于提交\s+`([0-9a-f]{7,40})`（(20\d\d-\d\d-\d\d)")
OWN_FILE = re.compile(r"https://github\.com/XIAOXUsop/([^/]+)/blob/(main|master)/([^#)\s]+)")
REPO_NAME = re.compile(r"https://github\.com/XIAOXUsop/([^/)]+)")


def check_document(readme):
    problems = []
    projects = list(PROJECT.finditer(readme))
    if len(projects) < 6:
        problems.append(f"expected at least 6 featured projects, found {len(projects)}")
    for index, match in enumerate(projects):
        end = projects[index + 1].start() if index + 1 < len(projects) else len(readme)
        section = readme[match.end():end]
        if not PROVENANCE.search(section):
            problems.append(f"{match[1]} has no dated verification commit")
    if "详见仓库内评测报告" in readme:
        problems.append("amlagent points to a deleted evaluation report")
    if "github.com/XIAOXUsop/amlagent#当前验证结果" not in readme:
        problems.append("amlagent evaluation numbers lack a README source link")
    return problems


def project_sources(readme):
    projects = list(PROJECT.finditer(readme))
    for index, match in enumerate(projects):
        end = projects[index + 1].start() if index + 1 < len(projects) else len(readme)
        source = PROVENANCE.search(readme[match.end():end])
        repo = REPO_NAME.search(match[0])
        if source and repo:
            yield repo[1], source[1]


def check_source_commits(readme, token):
    problems = []
    headers = {"User-Agent": "profile-link-check", "Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    for repo, commit in project_sources(readme):
        url = f"https://api.github.com/repos/XIAOXUsop/{repo}/commits/{commit}"
        request = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                if response.status != 200:
                    problems.append(f"{repo}: source commit {commit} returned HTTP {response.status}")
        except urllib.error.HTTPError as error:
            problems.append(f"{repo}: source commit {commit} returned HTTP {error.code}")
        except urllib.error.URLError as error:
            problems.append(f"{repo}: source commit {commit}: {error.reason}")
    return problems


def check_owned_file_links(readme, token):
    problems = []
    headers = {"User-Agent": "profile-link-check", "Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    for repo, branch, encoded_path in sorted(set(OWN_FILE.findall(readme))):
        path = urllib.parse.unquote(encoded_path)
        url = f"https://api.github.com/repos/XIAOXUsop/{repo}/contents/{urllib.parse.quote(path)}?ref={branch}"
        request = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                if response.status != 200:
                    problems.append(f"{repo}/{branch}/{path}: HTTP {response.status}")
        except urllib.error.HTTPError as error:
            problems.append(f"{repo}/{branch}/{path}: HTTP {error.code}")
        except urllib.error.URLError as error:
            problems.append(f"{repo}/{branch}/{path}: {error.reason}")
    return problems


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--online", action="store_true")
    args = parser.parse_args()
    readme = Path("README.md").read_text(encoding="utf-8")
    problems = check_document(readme)
    if args.online:
        problems.extend(check_source_commits(readme, os.environ.get("GH_TOKEN")))
        problems.extend(check_owned_file_links(readme, os.environ.get("GH_TOKEN")))
    if problems:
        for problem in problems:
            print(problem, file=sys.stderr)
        raise SystemExit(1)
    print("Profile project sources and links passed")
