"""
Task 2: Generates the final Visual Storytelling PDF Report
"""
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                  Image, HRFlowable, PageBreak)
from reportlab.lib.enums import TA_CENTER, TA_LEFT

doc = SimpleDocTemplate(
    "Task2_DataStorytelling_Report.pdf",
    pagesize=A4,
    topMargin=1.6*cm, bottomMargin=1.6*cm,
    leftMargin=1.8*cm, rightMargin=1.8*cm
)

styles = getSampleStyleSheet()
BLUE = colors.HexColor("#1a73e8")
ORANGE = colors.HexColor("#e8710a")
GREEN = colors.HexColor("#34a853")
DARK = colors.HexColor("#1e1e1e")
LIGHT_BG = colors.HexColor("#f0f4ff")

title_style = ParagraphStyle('Title', parent=styles['Title'],
    fontSize=22, textColor=BLUE, spaceAfter=4, alignment=TA_CENTER)
subtitle_style = ParagraphStyle('Sub', parent=styles['Normal'],
    fontSize=11, textColor=ORANGE, alignment=TA_CENTER, spaceAfter=14)
h2_style = ParagraphStyle('H2', parent=styles['Heading2'],
    fontSize=14, textColor=BLUE, spaceBefore=10, spaceAfter=6)
h3_style = ParagraphStyle('H3', parent=styles['Heading3'],
    fontSize=11.5, textColor=ORANGE, spaceBefore=4, spaceAfter=4)
body_style = ParagraphStyle('Body', parent=styles['Normal'],
    fontSize=10, textColor=DARK, leading=15, spaceAfter=4)
insight_style = ParagraphStyle('Insight', parent=styles['Normal'],
    fontSize=9.5, textColor=colors.HexColor("#333333"), leading=14,
    backColor=LIGHT_BG, borderPadding=8, spaceAfter=8)
kpi_label = ParagraphStyle('KPILabel', parent=styles['Normal'], fontSize=9,
    textColor=colors.grey, alignment=TA_CENTER)
kpi_value = ParagraphStyle('KPIValue', parent=styles['Normal'], fontSize=16,
    textColor=BLUE, alignment=TA_CENTER, fontName='Helvetica-Bold')

story = []

# ══════════════════════════════════════════════════
# COVER / TITLE PAGE
# ══════════════════════════════════════════════════
story.append(Spacer(1, 40))
story.append(Paragraph("DATA ANALYST INTERNSHIP", title_style))
story.append(Paragraph("Task 2: Data Visualization and Storytelling", subtitle_style))
story.append(HRFlowable(width="100%", thickness=2, color=ORANGE, spaceAfter=20))

story.append(Paragraph(
    "<b>Objective:</b> Create visualizations that convey a compelling business story "
    "from the Superstore sales dataset, highlighting trends, performance gaps, and "
    "actionable insights for decision-makers.", body_style))
story.append(Spacer(1, 10))

info_data = [
    ["Dataset", "Superstore Sales Data (1,850 orders, 2023–2025)"],
    ["Tools Used", "Python (Matplotlib, Seaborn, Pandas)"],
    ["Deliverable", "Visual Report (PDF) with 6 charts + storyboard summary"],
    ["Date", "30 June 2026"],
]
t = Table(info_data, colWidths=[4.5*cm, 11.5*cm])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (0,-1), LIGHT_BG),
    ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9.5),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#d0d0d0")),
    ('PADDING', (0,0), (-1,-1), 6),
]))
story.append(t)
story.append(Spacer(1, 20))

# KPI Summary Row
story.append(Paragraph("Executive Summary — Key Metrics", h2_style))
kpis = [
    ("$2.06M", "Total Sales"),
    ("$143.9K", "Total Profit"),
    ("7.0%", "Profit Margin"),
    ("1,850", "Total Orders"),
]
kpi_cells = []
for val, label in kpis:
    cell = [[Paragraph(val, kpi_value)], [Paragraph(label, kpi_label)]]
    kpi_cells.append(cell)

kpi_table_data = [[Table(c, rowHeights=[24,16]) for c in kpi_cells]]
kpi_t = Table(kpi_table_data, colWidths=[4*cm]*4)
kpi_t.setStyle(TableStyle([
    ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#d0d0d0")),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#d0d0d0")),
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#fafbff")),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('PADDING', (0,0), (-1,-1), 10),
]))
story.append(kpi_t)
story.append(PageBreak())

# ══════════════════════════════════════════════════
# Helper to add a chart section
# ══════════════════════════════════════════════════
def add_chart_section(num, title, img_path, insight_title, insight_text, img_width=16.5*cm, img_height=None):
    story.append(Paragraph(f"{num}. {title}", h2_style))
    img = Image(img_path, width=img_width, height=img_height or img_width*0.55)
    story.append(img)
    story.append(Spacer(1, 6))
    story.append(Paragraph(f"<b>📌 Key Takeaway — {insight_title}</b><br/>{insight_text}", insight_style))

# CHART 1
add_chart_section(
    1, "Monthly Sales Trend",
    "chart1_monthly_trend.png",
    "Seasonal Growth Pattern",
    "Sales show a clear upward trajectory from 2023 to 2025, with recurring peaks in Q4 "
    "(Nov–Dec), consistent with holiday shopping seasonality. This signals an opportunity "
    "to front-load inventory and marketing spend ahead of Q4 each year."
)
story.append(PageBreak())

# CHART 2
add_chart_section(
    2, "Sales by Product Sub-Category",
    "chart2_subcategory_sales.png",
    "Technology Leads Revenue",
    "Machines and Phones (Technology) are the top revenue-generating sub-categories, "
    "while Furnishings and Art (Office Supplies) lag behind. Technology should remain "
    "the primary investment focus for promotions and stock allocation."
)
story.append(PageBreak())

# CHART 3
add_chart_section(
    3, "Regional Performance: Sales vs. Profit",
    "chart3_regional_performance.png",
    "West Region Dominates",
    "The West region leads in both sales and profit, while the South region underperforms "
    "on both metrics. This gap suggests a need for region-specific strategies — potentially "
    "revisiting discount policy or marketing reach in the South."
)
story.append(PageBreak())

# CHART 4
add_chart_section(
    4, "Discount Impact on Profit",
    "chart4_discount_vs_profit.png",
    "Discounts Above 30% Erode Profit",
    "At 0% discount, average profit per order is $192.96. Once discounts exceed 30-40%, "
    "average profit turns negative (-$190.49). This is the single most actionable insight: "
    "capping discounts at 20-25% would protect margins significantly."
)
story.append(PageBreak())

# CHART 5
add_chart_section(
    5, "Sales Contribution by Customer Segment",
    "chart5_segment_donut.png",
    "Consumer Segment is the Core Revenue Driver",
    "The Consumer segment contributes 52.6% of total sales, more than Corporate and Home "
    "Office combined. Retention and loyalty programs targeted at consumers will have the "
    "highest revenue impact.",
    img_width=11*cm, img_height=11*cm
)
story.append(PageBreak())

# CHART 6
add_chart_section(
    6, "Year-over-Year Sales by Category",
    "chart6_yoy_category.png",
    "Consistent Category Mix Across Years",
    "Technology and Office Supplies have consistently outpaced Furniture every year. "
    "Furniture's slower contribution suggests it may need a pricing or marketing refresh "
    "to better compete for the unit volume increase."
)
story.append(PageBreak())

# ══════════════════════════════════════════════════
# STORYBOARD / SUMMARY SLIDE
# ══════════════════════════════════════════════════
story.append(Paragraph("Summary Storyboard — Business Narrative", h2_style))
story.append(Paragraph(
    "Putting the six charts together tells a clear story: <b>the business is growing "
    "steadily, led by the West region and the Consumer segment, with Technology as the "
    "star category — but profitability is being quietly undermined by aggressive "
    "discounting.</b>", body_style))
story.append(Spacer(1, 8))

story.append(Paragraph("The Story in 4 Acts", h3_style))
acts = [
    ["Act", "Insight", "Business Implication"],
    ["1. Growth", "Sales trending upward with strong Q4 seasonality", "Plan inventory & campaigns ahead of Q4"],
    ["2. Strength", "Technology sub-category & West region lead performance", "Double down on what's working"],
    ["3. Gap", "South region and Furniture category underperform", "Investigate root cause: pricing, demand, or reach"],
    ["4. Risk", "Discounts >30% turn profit negative", "Cap discount policy to protect margin"],
]
t5 = Table(acts, colWidths=[2.3*cm, 7*cm, 6.7*cm])
t5.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), BLUE),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 8.5),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#d0d0d0")),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f0f4ff")]),
    ('PADDING', (0,0), (-1,-1), 6),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(t5)
story.append(Spacer(1, 12))

story.append(Paragraph("Recommended Actions", h3_style))
actions = [
    "Cap discounts at 20-25% across all categories to safeguard profit margins.",
    "Increase marketing investment in the South region to close the performance gap.",
    "Maintain Technology category leadership through continued stock prioritization.",
    "Launch a Q3 pre-season campaign to extend the Q4 sales peak earlier in the year.",
    "Introduce a loyalty/rewards program targeting the high-value Consumer segment.",
]
for a in actions:
    story.append(Paragraph(f"✓ {a}", body_style))

story.append(Spacer(1, 16))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cccccc")))
story.append(Spacer(1, 6))
story.append(Paragraph(
    "Submitted as part of the DataX Labs Data Analyst Internship — Task 2",
    ParagraphStyle('footer', parent=styles['Normal'], fontSize=8,
                   textColor=colors.grey, alignment=TA_CENTER)
))

doc.build(story)
print("PDF report generated: Task2_DataStorytelling_Report.pdf")
