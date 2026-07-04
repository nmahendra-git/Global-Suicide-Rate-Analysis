"""
data_loader.py
---------------
Loads and cleans the global suicide rates dataset.

The commonly-used "Suicide Rates Overview 1985 to 2016" dataset (Kaggle/WHO)
has messy column names like "suicides/100k pop" and "gdp_for_year ($)".
This module standardizes them into clean snake_case names so the rest of
the code is easy to read.

Expected raw columns (case-insensitive, order doesn't matter):
    country, year, sex, age, suicides_no, population,
    suicides/100k pop, country-year, HDI for year,
    gdp_for_year ($), gdp_per_capita ($), generation

Usage:
    python src/data_loader.py                # sanity check on sample data
"""

import pandas as pd
import numpy as np

# Maps messy raw column names -> clean standardized names
COLUMN_RENAME_MAP = {
    "country": "country",
    "year": "year",
    "sex": "sex",
    "age": "age",
    "suicides_no": "suicides_no",
    "population": "population",
    "suicides/100k pop": "suicide_rate",
    "country-year": "country_year",
    "hdi for year": "hdi",
    "gdp_for_year ($)": "gdp_for_year",
    "gdp_per_capita ($)": "gdp_per_capita",
    "generation": "generation",
}


def load_data(path="data/sample_data.csv"):
    """Loads the raw CSV and returns a cleaned DataFrame.

    Cleaning steps:
      1. Standardize column names (lowercase, strip, rename via map)
      2. Convert numeric columns to proper numeric dtypes
      3. Drop the HDI column if it's mostly missing (common in this dataset)
      4. Standardize text columns (sex, age, generation) to consistent case
      5. Remove exact duplicate rows

    Args:
        path: path to the CSV file.

    Returns:
        A cleaned pandas DataFrame.
    """
    df = pd.read_csv(path)

    # Standardize column names: lowercase + strip whitespace, then rename
    df.columns = [c.strip().lower() for c in df.columns]
    df = df.rename(columns=COLUMN_RENAME_MAP)

    # Coerce numeric columns (some raw files store gdp_for_year as strings with commas)
    numeric_cols = ["year", "suicides_no", "population", "suicide_rate",
                     "hdi", "gdp_for_year", "gdp_per_capita"]
    for col in numeric_cols:
        if col in df.columns:
            if df[col].dtype == object:
                df[col] = df[col].astype(str).str.replace(",", "", regex=False)
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # HDI is missing for a large fraction of rows in the real dataset;
    # keep the column, but callers should be aware many rows will be NaN.

    # Standardize text
    for col in ["sex", "age", "generation", "country"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()
    if "sex" in df.columns:
        df["sex"] = df["sex"].str.lower()

    # Drop exact duplicate rows
    before = len(df)
    df = df.drop_duplicates()
    removed = before - len(df)
    if removed > 0:
        print(f"Removed {removed} duplicate rows")

    return df


def basic_quality_report(df):
    """Prints a quick data-quality summary: shape, dtypes, missing values."""
    print(f"Shape: {df.shape}")
    print("\nMissing values per column:")
    print(df.isna().sum())
    print("\nData types:")
    print(df.dtypes)
    print(f"\nYear range: {df['year'].min()} - {df['year'].max()}")
    print(f"Countries: {df['country'].nunique()}")


if __name__ == "__main__":
    df = load_data()
    basic_quality_report(df)
    print("\nSample rows:")
    print(df.head())
