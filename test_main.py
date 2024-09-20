from main import sample_df, summary
import unittest
import os


class Test_Main(unittest.TestCase):
    def test(self):
        self.assertTrue(sample_df is not None)
        self.assertEqual(summary["id"]["count"], 37137)

    def test_summary(self):
        self.assertTrue(summary is not None)

    def test_check_files(self):
        self.assertTrue("sample.png" in os.listdir("fig/"))
        self.assertTrue("sample2.png" in os.listdir("fig/"))
        self.assertTrue("summary.png" in os.listdir("fig/"))


if __name__ == "__main__":
    unittest.main()
