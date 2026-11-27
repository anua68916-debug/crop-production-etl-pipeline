import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import pandas as pd

from extract import extract


class TestExtract(unittest.TestCase):
    def test_missing_file_gives_clear_error(self):
        with TemporaryDirectory() as temp_dir:
            missing_path = Path(temp_dir) / "crop_production.csv"

            with self.assertRaisesRegex(
                FileNotFoundError, "Dataset not found"
            ):
                extract(missing_path)

    def test_missing_columns_gives_clear_error(self):
        with TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "wrong_columns.csv"
            pd.DataFrame({"Wrong_Column": [1]}).to_csv(
                csv_path, index=False
            )

            with self.assertRaisesRegex(
                ValueError, "Dataset is missing required columns"
            ):
                extract(csv_path)


if __name__ == "__main__":
    unittest.main()