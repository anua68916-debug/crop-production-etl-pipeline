import pandas as pd

def transform(df):
    start = len(df)

    # 1. Remove extra spaces from all text columns
    #    (Season looks like 'Kharif     ' in your data)
    text_cols = ["State_Name", "District_Name", "Season", "Crop"]
    for col in text_cols:
        df[col] = df[col].str.strip()

    # 2. Remove repeated rows
    df = df.drop_duplicates()

    # 3. Remove rows where Production is blank
    df = df.dropna(subset=["Production"])

    # 4. Remove rows with wrong values (area or production below zero or zero area)
    df = df[(df["Area"] > 0) & (df["Production"] >= 0)]

    # 5. Add a new column: yield (production per unit area)
    df["yield"] = (df["Production"] / df["Area"]).round(2)

    # 6. Add a new column: the unit of Production
    #    (Coconut is counted in nuts, other crops in tonnes)
    df["production_unit"] = df["Crop"].apply(
        lambda c: "nuts" if c == "Coconut" else "tonnes"
    )

    print("Rows before cleaning:", start)
    print("Rows after cleaning :", len(df))
    print("Rows removed        :", start - len(df))
    return df


if __name__ == "__main__":
    from extract import extract
    df = transform(extract())
    print("\nSeason values now:", list(df["Season"].unique()))
    print("\nFirst 5 rows:")
    print(df.head())