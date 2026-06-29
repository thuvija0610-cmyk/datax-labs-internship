import pandas as pd
import numpy as np

# Simulate a raw "Sales Data" dataset with intentional issues
np.random.seed(42)
n = 200

raw_data = {
    'Customer ID': list(range(1001, 1001 + n)) + [1005, 1020, 1035],  # duplicate IDs at end
    'Customer Name': ['Alice Johnson', 'BOB SMITH', 'carol white', 'David Lee', 'Emma Brown'] * 40 + ['BOB SMITH', 'alice johnson', 'EMMA BROWN'],
    'Gender': ['Female', 'Male', 'female', 'M', 'F', 'male', 'FEMALE', 'Male', 'female', 'M'] * 20 + ['Male', 'F', 'female'],
    'Age': list(np.random.randint(22, 65, n)) + [None, 29, 34],
    'Country': ['India', 'USA', 'india', 'United States', 'US', 'INDIA', 'usa', 'India', 'USA', 'India'] * 20 + ['India', 'USA', 'india'],
    'Purchase Date': (
        pd.date_range('2023-01-01', periods=n, freq='D').strftime('%d/%m/%Y').tolist() +
        ['2023-06-15', '15-07-2023', '2023/08/20']
    ),
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard'] * 40 + ['Laptop', 'Phone', 'Tablet'],
    'Sales Amount': list(np.random.uniform(500, 5000, n).round(2)) + [None, 1299.99, 2450.0],
    'Rating': list(np.random.randint(1, 6, n)) + [None, 4, 5],
}

df = pd.DataFrame(raw_data)
# Introduce ~8% missing values in some columns
for col in ['Age', 'Sales Amount', 'Rating']:
    mask = np.random.choice([True, False], size=len(df), p=[0.08, 0.92])
    df.loc[mask, col] = None

df.to_csv('/home/claude/task1_project/raw_sales_data.csv', index=False)
print("Raw dataset created:", df.shape)
print(df.head())
