# DataX Labs — Data Analyst Internship
## Task 1: Data Cleaning and Preprocessing

---

## Objective
Clean and prepare a raw sales dataset that contains missing values, duplicate rows, inconsistent text formats, mixed date formats, and incorrect data types — making it ready for analysis or modelling.

## Tools Used
- **Python 3.12**
- **Pandas** — data manipulation and cleaning
- **NumPy** — statistical operations
- **ReportLab** — PDF report generation

---

## Dataset
**Sales Data** — a simulated customer transactions dataset (203 rows × 9 columns) with the following intentional data quality issues:

| Issue | Details |
|---|---|
| Missing values | Age (20), Sales Amount (11), Rating (21) |
| Inconsistent casing | Customer names, Gender, Country |
| Non-standard categories | Gender: M/F/male/female; Country: US/USA/United States/india |
| Mixed date formats | dd/mm/yyyy, dd-mm-yyyy, yyyy-mm-dd |
| Wrong data types | Age and Rating stored as float instead of int |
| Messy column names | Spaces and mixed case |

---

## Files in This Repository

```
📁 task1-data-cleaning/
├── raw_sales_data.csv              # Original dirty dataset
├── cleaned_sales_data.csv          # Final cleaned dataset
├── data_cleaning.py                # Main Python cleaning script
├── generate_dataset.py             # Script to reproduce the raw dataset
├── generate_report.py              # Script to reproduce the PDF report
├── Task1_DataCleaning_Report.pdf   # Full summary report (PDF)
├── changes_summary.txt             # Log of all cleaning changes
└── README.md                       # This file
```

---

## How to Run

### 1. Install dependencies
```bash
pip install pandas numpy reportlab
```

### 2. Generate the raw dataset (optional — already included)
```bash
python generate_dataset.py
```

### 3. Run the cleaning script
```bash
python data_cleaning.py
```
This produces `cleaned_sales_data.csv` and `changes_summary.txt`.

### 4. Generate the PDF report (optional)
```bash
python generate_report.py
```

---

## Cleaning Steps Summary

1. **Removed duplicate rows** — `.drop_duplicates()`
2. **Standardized column names** — lowercase with underscores
3. **Standardized text** — Title Case for names; unified Gender (Male/Female) and Country (India/USA) values
4. **Handled missing values**:
   - Age → filled with **median** (robust to skew)
   - Sales Amount → filled with **per-product median** (preserves category patterns)
   - Rating → filled with **mode** (most frequent value)
5. **Fixed data types** — Age & Rating: float → int; Purchase Date → uniform dd-mm-yyyy
6. **Outlier detection** — IQR method applied on Sales Amount (no outliers found)

---

## Interview Question Answers

**1. What are missing values and how do you handle them?**
Missing values are cells with no data (NaN/None). They can be handled by: dropping rows/columns (if low %), filling with mean/median/mode, or using advanced imputation (KNN, regression). Choice depends on data type and distribution.

**2. How do you treat duplicate records?**
Use `.drop_duplicates()` in Pandas or `Remove Duplicates` in Excel. Always inspect duplicates first to understand if they're exact copies or near-duplicates needing fuzzy matching.

**3. Difference between dropna() and fillna() in Pandas?**
`dropna()` removes rows/columns containing NaN. `fillna(value)` replaces NaN with a specified value. Use `fillna` when losing rows would reduce data significantly.

**4. What is outlier treatment and why is it important?**
Outliers are extreme values that deviate significantly from the rest. They distort mean, regression lines, and ML models. Treatment options: remove, cap (Winsorize), log-transform, or keep with flagging.

**5. Explain the process of standardizing data.**
Standardizing means bringing values to a consistent format — e.g., unifying "Male/M/male" → "Male", date formats to one standard, and column names to lowercase.

**6. How do you handle inconsistent data formats (e.g., date/time)?**
Parse each variant using `pd.to_datetime()` with multiple format tries, then store in a single consistent format (e.g., dd-mm-yyyy string or datetime object).

**7. What are common data cleaning challenges?**
Missing data, duplicates, inconsistent formats, wrong data types, outliers, and domain-specific errors (e.g., negative ages, future birth dates).

**8. How can you check data quality?**
Use `.info()`, `.describe()`, `.isnull().sum()`, `.duplicated().sum()`, `.value_counts()`, and visualizations (histograms, boxplots) to profile the data.

---

*Submitted as part of the DataX Labs Data Analyst Internship — Task 1*
