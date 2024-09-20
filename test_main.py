from main import sample_df, summary
import unittest
import polars as pl
import os


class Test_Main(unittest.TestCase):
    def test_sample_df(self):
        # Check if the sample_df is not None
        self.assertTrue(sample_df is not None)
        # Verify the count of the 'id' column in the summary
        self.assertEqual(
            summary.filter(pl.col("statistic") == "count").get_column("id").item(),
            37137,
        )

    def test_summary(self):
        # Check if the summary is not None
        self.assertTrue(summary is not None)

    def test_check_files(self):
        # Check if the required files are present in the "fig/" directory
        self.assertTrue("sample.png" in os.listdir("fig/"))
        self.assertTrue("sample2.png" in os.listdir("fig/"))
        self.assertTrue("summary.png" in os.listdir("fig/"))


if __name__ == "__main__":
    unittest.main()
