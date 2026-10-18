import sqlite3

def load(df, db="crops.db"):
    conn = sqlite3.connect(db)
    df.to_sql("crop_production", conn, if_exists="replace", index=False)
    conn.close()
    print("Clean data saved in", db, "| table: crop_production | rows:", len(df))


if __name__ == "__main__":
    from extract import extract
    from transform import transform

    clean = transform(extract())
    load(clean)

    # Check: ask the database how many rows it has
    conn = sqlite3.connect("crops.db")
    count = conn.execute("SELECT COUNT(*) FROM crop_production").fetchone()[0]
    print("Rows found inside database:", count)
    conn.close()