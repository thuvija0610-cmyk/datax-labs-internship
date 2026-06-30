"""
Generates a realistic Superstore-style sales dataset for Task 2
"""
import pandas as pd
import numpy as np

np.random.seed(7)

regions = ['West', 'East', 'Central', 'South']
states = {
    'West': ['California', 'Washington', 'Oregon', 'Arizona'],
    'East': ['New York', 'Pennsylvania', 'New Jersey', 'Massachusetts'],
    'Central': ['Texas', 'Illinois', 'Michigan', 'Ohio'],
    'South': ['Florida', 'Georgia', 'North Carolina', 'Tennessee']
}
categories = {
    'Furniture': ['Chairs', 'Tables', 'Bookcases', 'Furnishings'],
    'Office Supplies': ['Binders', 'Paper', 'Storage', 'Art'],
    'Technology': ['Phones', 'Machines', 'Accessories', 'Copiers']
}
segments = ['Consumer', 'Corporate', 'Home Office']
ship_modes = ['Standard Class', 'Second Class', 'First Class', 'Same Day']

n = 1850
rows = []
order_date_range = pd.date_range('2023-01-01', '2025-12-31', freq='D')

for i in range(n):
    region = np.random.choice(regions, p=[0.32, 0.28, 0.22, 0.18])
    state = np.random.choice(states[region])
    category = np.random.choice(list(categories.keys()), p=[0.22, 0.52, 0.26])
    sub_category = np.random.choice(categories[category])
    segment = np.random.choice(segments, p=[0.51, 0.30, 0.19])
    ship_mode = np.random.choice(ship_modes, p=[0.6, 0.2, 0.15, 0.05])
    order_date = np.random.choice(order_date_range)
    order_date = pd.Timestamp(order_date)
    ship_date = order_date + pd.Timedelta(days=np.random.randint(1, 8))

    # Category-based pricing patterns
    base_price = {'Furniture': 250, 'Office Supplies': 35, 'Technology': 420}[category]
    quantity = np.random.randint(1, 10)
    sales = round(base_price * quantity * np.random.uniform(0.6, 1.8), 2)

    # Discount patterns (higher discounts -> lower or negative profit)
    discount = np.random.choice([0, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5], p=[0.35,0.2,0.15,0.12,0.1,0.05,0.03])
    margin_rate = {'Furniture': 0.12, 'Office Supplies': 0.28, 'Technology': 0.18}[category]
    profit = round(sales * margin_rate - sales * discount * 0.8, 2)

    rows.append([
        f"ORD-{10000+i}", order_date, ship_date, ship_mode, segment, region, state,
        category, sub_category, sales, quantity, discount, profit
    ])

df = pd.DataFrame(rows, columns=[
    'Order ID', 'Order Date', 'Ship Date', 'Ship Mode', 'Segment', 'Region', 'State',
    'Category', 'Sub-Category', 'Sales', 'Quantity', 'Discount', 'Profit'
])

df.to_csv('superstore.csv', index=False)
print("Dataset created:", df.shape)
print(df.head())
print("\nTotal Sales:", df['Sales'].sum())
print("Total Profit:", df['Profit'].sum())
