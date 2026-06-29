"""
Task 1: Data Cleaning and Preprocessing
DataX Labs - Data Analyst Internship

Dataset: Sales Data (simulated raw dataset with common real-world issues)
Tools: Python (Pandas, NumPy)
Author: Data Analyst Intern
Date: 2026-06-29
"""

import pandas as pd
import numpy as np

# ─────────────────────────────────────────────
# STEP 1: Load Raw Dataset
# ─────────────────────────────────────────────
print("=" * 60)
print("TASK 1: DATA CLEANING AND PREPROCESSING")
print("=" * 60)

df = pd.read_csv("raw_sales_data.csv")
print(f"\n[LOAD] Raw dataset shape: {df.shape}")
print(f"Columns: {list(df.columns)}\n")

changes_log = []

# ─────────────────────────────────────────────
# STEP 2: Initial Inspection
# ─────────────────────────────────────────────
print("─" * 40)
print("INITIAL DATA INSPECTION")
print("─" * 40)
print(df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print(f"\nDuplicate Rows: {df.duplicated().sum()}")

# ─────────────────────────────────────────────
# STEP 3: Handle Duplicate Rows
# ─────────────────────────────────────────────
before = len(df)
df.drop_duplicates(inplace=True)
after = len(df)
removed = before - after
changes_log.append(f"Removed {removed} duplicate rows (before: {before}, after: {after})")
print(f"\n[DUPLICATES] Removed {removed} duplicate rows.")

# ─────────────────────────────────────────────
# STEP 4: Standardize Column Headers
# ─────────────────────────────────────────────
original_cols = list(df.columns)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
changes_log.append(f"Standardized column names to lowercase with underscores: {list(df.columns)}")
print(f"\n[COLUMNS] Renamed columns: {list(df.columns)}")

# ─────────────────────────────────────────────
# STEP 5: Standardize Text Columns
# ─────────────────────────────────────────────

# Customer Name → Title Case
df['customer_name'] = df['customer_name'].str.strip().str.title()
changes_log.append("Standardized 'customer_name' to Title Case.")

# Gender → Unified values: Male / Female
gender_map = {
    'male': 'Male', 'm': 'Male',
    'female': 'Female', 'f': 'Female',
}
df['gender'] = df['gender'].str.strip().str.lower().map(gender_map)
null_gender = df['gender'].isnull().sum()
if null_gender > 0:
    df['gender'].fillna('Unknown', inplace=True)
changes_log.append(f"Standardized 'gender' values to Male/Female/Unknown. Filled {null_gender} unknowns.")
print(f"\n[GENDER] Unique values after cleaning: {df['gender'].unique()}")

# Country → Unified values
country_map = {
    'india': 'India', 'INDIA': 'India',
    'usa': 'USA', 'us': 'USA', 'united states': 'USA', 'United States': 'USA',
}
df['country'] = df['country'].str.strip().str.lower().map(country_map)
null_country = df['country'].isnull().sum()
if null_country > 0:
    df['country'].fillna('Unknown', inplace=True)
changes_log.append(f"Standardized 'country' values. Filled {null_country} unknowns.")
print(f"[COUNTRY] Unique values after cleaning: {df['country'].unique()}")

# ─────────────────────────────────────────────
# STEP 6: Handle Missing Values
# ─────────────────────────────────────────────
print(f"\n[MISSING] Before handling:\n{df.isnull().sum()}")

# Age → fill with median (robust to outliers)
age_median = df['age'].median()
null_age = df['age'].isnull().sum()
df['age'] = df['age'].fillna(age_median)
changes_log.append(f"Filled {null_age} missing 'age' values with median ({age_median:.0f}).")

# Sales Amount → fill with median per product category
null_sales = df['sales_amount'].isnull().sum()
df['sales_amount'] = df.groupby('product')['sales_amount'].transform(
    lambda x: x.fillna(x.median())
)
changes_log.append(f"Filled {null_sales} missing 'sales_amount' values with per-product median.")

# Rating → fill with mode (most common rating)
rating_mode = df['rating'].mode()[0]
null_rating = df['rating'].isnull().sum()
df['rating'] = df['rating'].fillna(rating_mode)
changes_log.append(f"Filled {null_rating} missing 'rating' values with mode ({rating_mode:.0f}).")

print(f"\n[MISSING] After handling:\n{df.isnull().sum()}")

# ─────────────────────────────────────────────
# STEP 7: Fix Data Types
# ─────────────────────────────────────────────

# Age → integer (ensure no NaN before cast)
df['age'] = df['age'].fillna(df['age'].median()).astype(int)

# Sales Amount → float (round to 2 decimal places)
df['sales_amount'] = df['sales_amount'].round(2).astype(float)

# Rating → integer (ensure no NaN before cast)
df['rating'] = df['rating'].fillna(df['rating'].mode()[0]).astype(int)

# Purchase Date → Parse mixed formats to datetime
def parse_date(date_str):
    for fmt in ('%d/%m/%Y', '%d-%m-%Y', '%Y-%m-%d', '%Y/%m/%d'):
        try:
            return pd.to_datetime(date_str, format=fmt)
        except:
            pass
    return pd.NaT

df['purchase_date'] = df['purchase_date'].apply(parse_date)
# Standardize to dd-mm-yyyy string format
df['purchase_date'] = df['purchase_date'].dt.strftime('%d-%m-%Y')

changes_log.append("Converted and standardized 'purchase_date' to dd-mm-yyyy format.")
changes_log.append("Fixed data types: age→int, sales_amount→float, rating→int.")
print(f"\n[DTYPES] Final data types:\n{df.dtypes}")

# ─────────────────────────────────────────────
# STEP 8: Outlier Check (Sales Amount)
# ─────────────────────────────────────────────
Q1 = df['sales_amount'].quantile(0.25)
Q3 = df['sales_amount'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[(df['sales_amount'] < lower) | (df['sales_amount'] > upper)]
changes_log.append(f"Outlier check on 'sales_amount': {len(outliers)} outliers detected (kept, flagged only). Range: [{lower:.2f}, {upper:.2f}]")
print(f"\n[OUTLIERS] Sales Amount outliers: {len(outliers)} rows (flagged, not removed)")

# ─────────────────────────────────────────────
# STEP 9: Final Validation
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print("FINAL CLEANED DATASET SUMMARY")
print("=" * 60)
print(f"Shape: {df.shape}")
print(f"Missing values: {df.isnull().sum().sum()}")
print(f"Duplicates: {df.duplicated().sum()}")
print(f"\nSample (first 5 rows):\n{df.head().to_string()}")
print(f"\nDescriptive Statistics:\n{df.describe().to_string()}")

# ─────────────────────────────────────────────
# STEP 10: Save Cleaned Dataset
# ─────────────────────────────────────────────
df.to_csv("cleaned_sales_data.csv", index=False)
print(f"\n[SAVED] Cleaned dataset saved to: cleaned_sales_data.csv")

# ─────────────────────────────────────────────
# STEP 11: Print Changes Summary
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print("SUMMARY OF CHANGES MADE")
print("=" * 60)
for i, change in enumerate(changes_log, 1):
    print(f"{i}. {change}")

# Save changes log
with open("changes_summary.txt", "w") as f:
    f.write("DATA CLEANING CHANGES SUMMARY\n")
    f.write("=" * 50 + "\n\n")
    for i, change in enumerate(changes_log, 1):
        f.write(f"{i}. {change}\n")

print("\n[DONE] All cleaning steps completed successfully!")
