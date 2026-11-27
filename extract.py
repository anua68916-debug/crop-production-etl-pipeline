from pathlib import Path
import pandas as pd

def extract(path="data/crop_production.csv"):
    csv_path = Path(path)

    if not csv_path.is_file():
        raise FileNotFoundError(
            f"Dataset not found at '{csv_path}'. "
            "Put crop_production.csv in the data folder."
        )

    df = pd.read_csv(csv_path)

    required_columns = {
        "State_Name",
        "District_Name",
        "Season",
        "Crop",
        "Area",
        "Production",
    }
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Dataset is missing required columns: {missing}")

    print("Extracted rows:", len(df))
    return df

# This part runs only when you run this file directly
if __name__ == "__main__":
    df = extract()
    print("\nShape (rows, columns):", df.shape)
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nBlank cells per column:")
    print(df.isna().sum())
    print("\nDuplicate rows:", df.duplicated().sum())
    print("\nSeason values:", list(df["Season"].unique()))
    print("\nNumber of states:", df["State_Name"].nunique())