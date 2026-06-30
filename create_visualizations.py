"""
Task 2: Data Visualization and Storytelling
Generates a set of polished business charts from Superstore sales data.
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import numpy as np

# ── Style Setup ──────────────────────────────────────────
sns.set_theme(style="whitegrid", font_scale=1.0)
PALETTE = ['#1a73e8', '#e8710a', '#34a853', '#ea4335', '#9c27b0']
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['figure.facecolor'] = 'white'

df = pd.read_csv('superstore.csv', parse_dates=['Order Date', 'Ship Date'])
df['Month'] = df['Order Date'].dt.to_period('M').dt.to_timestamp()
df['Year'] = df['Order Date'].dt.year

# ══════════════════════════════════════════════════════════
# CHART 1: Monthly Sales Trend (Line Chart)
# ══════════════════════════════════════════════════════════
monthly = df.groupby('Month')['Sales'].sum().reset_index()

fig, ax = plt.subplots(figsize=(11, 5))
ax.plot(monthly['Month'], monthly['Sales'], color=PALETTE[0], linewidth=2.5, marker='o', markersize=4)
ax.fill_between(monthly['Month'], monthly['Sales'], alpha=0.08, color=PALETTE[0])
ax.set_title('Monthly Sales Trend (2023–2025)', fontsize=15, fontweight='bold', pad=15)
ax.set_xlabel('')
ax.set_ylabel('Sales ($)', fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x/1000:.0f}K'))
ax.spines[['top', 'right']].set_visible(False)
peak = monthly.loc[monthly['Sales'].idxmax()]
ax.annotate(f"Peak: ${peak['Sales']/1000:.0f}K", xy=(peak['Month'], peak['Sales']),
            xytext=(10, 15), textcoords='offset points', fontsize=9, fontweight='bold',
            color=PALETTE[1], arrowprops=dict(arrowstyle='->', color=PALETTE[1]))
plt.tight_layout()
plt.savefig('chart1_monthly_trend.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 1 saved: Monthly Sales Trend")

# ══════════════════════════════════════════════════════════
# CHART 2: Sales by Category & Sub-Category (Horizontal Bar)
# ══════════════════════════════════════════════════════════
cat_sales = df.groupby(['Category', 'Sub-Category'])['Sales'].sum().reset_index()
cat_sales = cat_sales.sort_values('Sales', ascending=True)
cat_color_map = {'Furniture': PALETTE[0], 'Office Supplies': PALETTE[1], 'Technology': PALETTE[2]}
colors = cat_sales['Category'].map(cat_color_map)

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(cat_sales['Sub-Category'], cat_sales['Sales'], color=colors)
ax.set_title('Sales by Product Sub-Category', fontsize=15, fontweight='bold', pad=15)
ax.set_xlabel('Sales ($)', fontsize=11)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x/1000:.0f}K'))
ax.spines[['top', 'right']].set_visible(False)
for bar, val in zip(bars, cat_sales['Sales']):
    ax.text(val + 3000, bar.get_y() + bar.get_height()/2, f'${val/1000:.0f}K',
            va='center', fontsize=9)
handles = [plt.Rectangle((0,0),1,1, color=c) for c in cat_color_map.values()]
ax.legend(handles, cat_color_map.keys(), loc='lower right', frameon=True, fontsize=9)
plt.tight_layout()
plt.savefig('chart2_subcategory_sales.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 2 saved: Sales by Sub-Category")

# ══════════════════════════════════════════════════════════
# CHART 3: Regional Performance — Sales vs Profit (Grouped Bar)
# ══════════════════════════════════════════════════════════
region_perf = df.groupby('Region')[['Sales', 'Profit']].sum().reset_index()
region_perf = region_perf.sort_values('Sales', ascending=False)

fig, ax = plt.subplots(figsize=(9, 5.5))
x = np.arange(len(region_perf))
width = 0.35
b1 = ax.bar(x - width/2, region_perf['Sales'], width, label='Sales', color=PALETTE[0])
b2 = ax.bar(x + width/2, region_perf['Profit']*5, width, label='Profit (×5 scale)', color=PALETTE[2])
ax.set_title('Regional Performance: Sales vs. Profit', fontsize=15, fontweight='bold', pad=15)
ax.set_xticks(x)
ax.set_xticklabels(region_perf['Region'], fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x/1000:.0f}K'))
ax.spines[['top', 'right']].set_visible(False)
ax.legend(frameon=True, fontsize=9)
for bars in [b1, b2]:
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, h + 5000, f'${h/1000:.0f}K' if bar in b1 else f'${h/5/1000:.0f}K',
                ha='center', fontsize=8)
plt.tight_layout()
plt.savefig('chart3_regional_performance.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 3 saved: Regional Performance")

# ══════════════════════════════════════════════════════════
# CHART 4: Discount Impact on Profit (Scatter)
# ══════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(10, 5.5))
for cat, color in cat_color_map.items():
    subset = df[df['Category'] == cat]
    ax.scatter(subset['Discount'], subset['Profit'], alpha=0.4, s=25, color=color, label=cat)
ax.axhline(0, color='#666666', linewidth=1, linestyle='--')
ax.set_title('Discount Impact on Profit', fontsize=15, fontweight='bold', pad=15)
ax.set_xlabel('Discount Rate', fontsize=11)
ax.set_ylabel('Profit ($)', fontsize=11)
ax.xaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
ax.spines[['top', 'right']].set_visible(False)
ax.legend(frameon=True, fontsize=9)
ax.annotate('Profit turns negative\nat high discounts', xy=(0.45, -50), xytext=(0.25, -180),
            fontsize=9, fontweight='bold', color=PALETTE[3],
            arrowprops=dict(arrowstyle='->', color=PALETTE[3]))
plt.tight_layout()
plt.savefig('chart4_discount_vs_profit.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 4 saved: Discount vs Profit")

# ══════════════════════════════════════════════════════════
# CHART 5: Customer Segment Contribution (Donut Chart)
# ══════════════════════════════════════════════════════════
seg_sales = df.groupby('Segment')['Sales'].sum().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(7.5, 7.5))
wedges, texts, autotexts = ax.pie(
    seg_sales, labels=seg_sales.index, autopct='%1.1f%%', startangle=90,
    colors=PALETTE[:3], pctdistance=0.8, textprops={'fontsize': 11},
    wedgeprops=dict(width=0.4, edgecolor='white', linewidth=2)
)
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
ax.set_title('Sales Contribution by Customer Segment', fontsize=15, fontweight='bold', pad=20)
ax.text(0, 0, f"${seg_sales.sum()/1e6:.2f}M\nTotal Sales", ha='center', va='center',
        fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('chart5_segment_donut.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 5 saved: Segment Donut")

# ══════════════════════════════════════════════════════════
# CHART 6: Year-over-Year Category Growth (Stacked Bar)
# ══════════════════════════════════════════════════════════
yearly_cat = df.groupby(['Year', 'Category'])['Sales'].sum().unstack()

fig, ax = plt.subplots(figsize=(9, 5.5))
yearly_cat.plot(kind='bar', stacked=True, ax=ax, color=[cat_color_map[c] for c in yearly_cat.columns])
ax.set_title('Year-over-Year Sales by Category', fontsize=15, fontweight='bold', pad=15)
ax.set_xlabel('')
ax.set_ylabel('Sales ($)', fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x/1000:.0f}K'))
ax.spines[['top', 'right']].set_visible(False)
plt.xticks(rotation=0)
ax.legend(title='', frameon=True, fontsize=9)
plt.tight_layout()
plt.savefig('chart6_yoy_category.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 6 saved: YoY Category Growth")

print("\nAll 6 charts generated successfully.")

# ── Print key insights for the report ──
print("\n" + "="*50)
print("KEY INSIGHTS")
print("="*50)
print(f"Total Sales: ${df['Sales'].sum():,.0f}")
print(f"Total Profit: ${df['Profit'].sum():,.0f}")
print(f"Overall Profit Margin: {df['Profit'].sum()/df['Sales'].sum()*100:.1f}%")
print(f"Top Region by Sales: {region_perf.iloc[0]['Region']} (${region_perf.iloc[0]['Sales']:,.0f})")
print(f"Top Sub-Category: {cat_sales.iloc[-1]['Sub-Category']} (${cat_sales.iloc[-1]['Sales']:,.0f})")
print(f"Top Segment: {seg_sales.index[0]} ({seg_sales.iloc[0]/seg_sales.sum()*100:.1f}%)")
high_disc_profit = df[df['Discount'] >= 0.4]['Profit'].mean()
low_disc_profit = df[df['Discount'] == 0]['Profit'].mean()
print(f"Avg profit at 0% discount: ${low_disc_profit:.2f}")
print(f"Avg profit at 40%+ discount: ${high_disc_profit:.2f}")
