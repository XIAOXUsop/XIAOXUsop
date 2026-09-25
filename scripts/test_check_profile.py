import unittest

from check_profile import check_document, project_sources


class ProfileFactsTest(unittest.TestCase):
    def test_missing_verification_commit_is_reported(self):
        readme = "### [demo](https://github.com/XIAOXUsop/demo)\nCI ✅\n"
        self.assertTrue(any("dated verification" in p for p in check_document(readme)))

    def test_deleted_report_reference_is_reported(self):
        readme = "详见仓库内评测报告"
        self.assertTrue(any("deleted evaluation report" in p for p in check_document(readme)))

    def test_source_commit_is_taken_from_its_own_project_section(self):
        readme = (
            "### [one](https://github.com/XIAOXUsop/one)\n"
            "验证于提交 `abc1234`（2026-09-22）\n"
            "### [two](https://github.com/XIAOXUsop/two)\n"
            "验证于提交 `def5678`（2026-09-22）\n"
        )
        self.assertEqual(list(project_sources(readme)), [("one", "abc1234"), ("two", "def5678")])


if __name__ == "__main__":
    unittest.main()
