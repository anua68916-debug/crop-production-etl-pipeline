# Crop Production ETL Pipeline

A beginner data engineering project that builds an ETL pipeline using Python, Pandas and SQLite on real crop production data from India.

## What it does
1. Extract: reads the raw CSV file (246,091 rows) with Pandas
2. Transform: removes extra spaces, blank values and wrong values, and adds new columns (yield, production unit)
3. Load: saves the clean data (242,361 rows) into an SQLite database
4. Analyse: runs SQL queries and draws a chart

## Tools used
Python, Pandas, SQLite, SQL, Matplotlib

## Dataset
Crop Production in India (Kaggle, by abhinand05)
https://www.kaggle.com/datasets/abhinand05/crop-production-in-india

Download crop_production.csv and put it inside a folder named data.

## How to run
1. pip install pandas matplotlib
2. Put crop_production.csv inside the data folder
3. python main.py

## Files
- extract.py: reads the data
- transform.py: cleans the data
- load.py: saves it into the database
- analyse.py: SQL queries and chart
- main.py: runs the whole pipeline