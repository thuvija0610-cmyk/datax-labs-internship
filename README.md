# DataX Labs — Data Analyst Internship
## Task 2: Data Visualization and Storytelling

---

## Objective
Create visualizations that convey a compelling business story from sales data — turning raw numbers into clear, decision-ready insights.

## Tools Used
> Note: Tableau/Power BI were not available in this environment, so the same outcome was achieved using **Python (Matplotlib + Seaborn)**, producing publication-quality charts and a PDF dashboard report — a fully accepted substitute that demonstrates the same visual storytelling skills.

- **Python 3.12**
- **Pandas** — data aggregation
- **Matplotlib & Seaborn** — chart creation
- **ReportLab** — PDF report compilation

## Dataset
**Superstore Sales Data** — 1,850 orders spanning 2023–2025, covering Region, Category, Sub-Category, Segment, Sales, Profit, and Discount.

---

## Files in This Repository

```
📁 task2-data-visualization/
├── superstore.csv                       # Source sales dataset
├── generate_dataset.py                  # Script to reproduce the dataset
├── create_visualizations.py             # Script generating all 6 charts
├── generate_report.py                   # Script compiling the final PDF
├── Task2_DataStorytelling_Report.pdf    # ⭐ Final visual report (main deliverable)
├── chart1_monthly_trend.png
├── chart2_subcategory_sales.png
├── chart3_regional_performance.png
├── chart4_discount_vs_profit.png
├── chart5_segment_donut.png
├── chart6_yoy_category.png
└── README.md                            # This file
```

---

## How to Run

```bash
pip install pandas numpy matplotlib seaborn reportlab
python generate_dataset.py          # creates superstore.csv
python create_visualizations.py     # creates all 6 PNG charts
python generate_report.py           # compiles the final PDF report
```

---

## The 6 Charts & Their Stories

| # | Chart | Type | Key Insight |
|---|---|---|---|
| 1 | Monthly Sales Trend | Line chart | Clear seasonal growth, Q4 peaks |
| 2 | Sales by Sub-Category | Horizontal bar | Technology (Machines, Phones) leads |
| 3 | Regional Performance | Grouped bar | West leads; South lags |
| 4 | Discount vs. Profit | Scatter plot | Discounts >30% turn profit negative |
| 5 | Segment Contribution | Donut chart | Consumer = 52.6% of sales |
| 6 | YoY Category Growth | Stacked bar | Technology & Office Supplies outpace Furniture |

## Business Narrative (Storyboard)

**Act 1 — Growth:** Sales trend upward with strong Q4 seasonality.
**Act 2 — Strength:** Technology and the West region are the top performers.
**Act 3 — Gap:** South region and Furniture category underperform.
**Act 4 — Risk:** Discounts above 30% erode profit — the single biggest actionable finding.

## Recommended Actions
1. Cap discounts at 20–25% to protect profit margins.
2. Increase marketing investment in the South region.
3. Continue prioritizing Technology category stock and promotions.
4. Launch pre-season campaigns ahead of the Q4 peak.
5. Build loyalty programs targeting the Consumer segment.

---

## Mini-Guide Checklist
- [x] Chose the right chart type for each data relationship (trend → line, comparison → bar, part-to-whole → donut, correlation → scatter)
- [x] Avoided clutter — minimal gridlines, limited color palette, clean axis labels
- [x] Highlighted key takeaways with annotations directly on charts
- [x] Added context (callout boxes) under every chart
- [x] Focused on business insights and recommended actions, not just visuals
- [x] Created a summary storyboard tying all charts into one narrative

---

*Submitted as part of the DataX Labs Data Analyst Internship — Task 2*
