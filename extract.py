import pandas as pd

def extract(path="data/crop_production.csv"):
    df = pd.read_csv(path)
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