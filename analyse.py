import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Coconut is counted in nuts (not tonnes), so we leave it out of tonnes comparisons
queries = {
    "1. Total clean records":
        "SELECT COUNT(*) AS total_records FROM crop_production",

    "2. Records per season":
        "SELECT Season, COUNT(*) AS records FROM crop_production "
        "GROUP BY Season ORDER BY records DESC",

    "3. Top 5 states by total production (tonnes)":
        "SELECT State_Name, ROUND(SUM(Production)) AS total_production "
        "FROM crop_production WHERE production_unit = 'tonnes' "
        "GROUP BY State_Name ORDER BY total_production DESC LIMIT 5",

    "4. Top 10 crops by total production (tonnes)":
        "SELECT Crop, ROUND(SUM(Production)) AS total_production "
        "FROM crop_production WHERE production_unit = 'tonnes' "
        "GROUP BY Crop ORDER BY total_production DESC LIMIT 10",

    "5. Karnataka: top 5 crops by average yield":
        "SELECT Crop, ROUND(AVG(yield), 2) AS avg_yield, COUNT(*) AS records "
        "FROM crop_production WHERE State_Name = 'Karnataka' "
        "AND production_unit = 'tonnes' "
        "GROUP BY Crop HAVING COUNT(*) >= 20 "
        "ORDER BY avg_yield DESC LIMIT 5",
}

def analyse(db="crops.db"):
    conn = sqlite3.connect(db)

    for title, sql in queries.items():
        print("\n" + title)
        print(pd.read_sql_query(sql, conn).to_string(index=False))

    # Chart: top 10 crops by production
    data = pd.read_sql_query(queries["4. Top 10 crops by total production (tonnes)"], conn)
    plt.figure(figsize=(10, 5))
    plt.bar(data["Crop"], data["total_production"], color="teal")
    plt.title("Top 10 Crops by Total Production (tonnes)")
    plt.xlabel("Crop")
    plt.ylabel("Production (tonnes)")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    plt.savefig("chart.png")
    print("\nChart saved as chart.png")

    conn.close()


if __name__ == "__main__":
    analyse()