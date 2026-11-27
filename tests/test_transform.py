import unittest

import pandas as pd

from transform import transform


class TestTransform(unittest.TestCase):
    def test_cleans_rows_and_calculates_yield_and_units(self):
        rows = [
            {
                "State_Name": " Karnataka ",
                "District_Name": " Mysuru ",
                "Crop_Year": 2020,
                "Season": " Kharif ",
                "Crop": " Rice ",
                "Area": 2,
                "Production": 10,
            },
            # Duplicate row; it should be removed.
            {
                "State_Name": " Karnataka ",
                "District_Name": " Mysuru ",
                "Crop_Year": 2020,
                "Season": " Kharif ",
                "Crop": " Rice ",
                "Area": 2,
                "Production": 10,
            },
            # These rows should be removed by the cleaning rules.
            {
                "State_Name": "Karnataka", "District_Name": "Mysuru",
                "Crop_Year": 2020, "Season": "Rabi", "Crop": "Wheat",
                "Area": 1, "Production": None,
            },
            {
                "State_Name": "Karnataka", "District_Name": "Mysuru",
                "Crop_Year": 2020, "Season": "Rabi", "Crop": "Wheat",
                "Area": None, "Production": 5,
            },
            {
                "State_Name": "Karnataka", "District_Name": "Mysuru",
                "Crop_Year": 2020, "Season": "Rabi", "Crop": "Wheat",
                "Area": 0, "Production": 5,
            },
            {
                "State_Name": "Karnataka", "District_Name": "Mysuru",
                "Crop_Year": 2020, "Season": "Rabi", "Crop": "Wheat",
                "Area": 1, "Production": -5,
            },
            # A valid coconut row checks its separate unit label.
            {
                "State_Name": "Karnataka", "District_Name": "Mysuru",
                "Crop_Year": 2020, "Season": "Whole Year", "Crop": "Coconut",
                "Area": 2, "Production": 200,
            },
        ]

        cleaned = transform(pd.DataFrame(rows))

        self.assertEqual(len(cleaned), 2)

        rice = cleaned[cleaned["Crop"] == "Rice"].iloc[0]
        self.assertEqual(rice["State_Name"], "Karnataka")
        self.assertEqual(rice["District_Name"], "Mysuru")
        self.assertEqual(rice["yield"], 5)
        self.assertEqual(rice["production_unit"], "tonnes")

        coconut = cleaned[cleaned["Crop"] == "Coconut"].iloc[0]
        self.assertEqual(coconut["yield"], 100)
        self.assertEqual(coconut["production_unit"], "nuts")


if __name__ == "__main__":
    unittest.main()