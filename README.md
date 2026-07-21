# 📊 Revenue Leak & Growth Opportunity Analyzer

A complete Business Analytics project that identifies revenue leakages and growth opportunities using **SQL**, **Python**, **Pandas**, and **SQLite**.

The project simulates a real retail business environment by generating transactional data, loading it into a relational database, performing business analysis with SQL and Pandas, and automatically generating business reports.

---

# 🎯 Project Objective

Businesses often lose revenue due to:

- High discounts
- Poor-performing products
- Regional performance differences
- Customer segment behavior
- Inefficient sales channels
- Revenue trends over time

This project analyzes these factors and provides actionable business insights to support better decision-making.

---

# 🛠️ Tech Stack

- Python
- Pandas
- SQL
- SQLite
- CSV
- VS Code
- Git & GitHub

---

# 📂 Project Structure

Revenue-Leak-Growth-Opportunity-Analyzer/
│
├── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   ├── products.csv
│   │   ├── orders.csv
│   │   ├── order_items.csv
│   │   ├── deliveries.csv
│   │   └── returns.csv
│   │
│   ├── processed/
│   │   ├── customers.csv
│   │   ├── products.csv
│   │   ├── orders.csv
│   │   ├── order_items.csv
│   │   ├── deliveries.csv
│   │   └── returns.csv
│   │
│   └── database/
│       └── retail_sales.db
│
├── reports/
│   ├── top_products.csv
│   ├── revenue_by_region.csv
│   ├── revenue_by_segment.csv
│   ├── discount_analysis.csv
│   ├── sales_channel_analysis.csv
│   ├── monthly_revenue_trend.csv
│   ├── data_quality_report.csv
│   └── business_insights.md
│
├── screenshots/
│   ├── database_tables.png
│   ├── sql_queries.png
│   ├── pandas_analysis.png
│   ├── reports.png
│   └── project_structure.png
│
├── sql/
│   ├── 01_schema.sql
│   ├── 02_total_revenue.sql
│   ├── 03_top_revenue_products.sql
│   ├── 04_revenue_by_category.sql
│   ├── 05_revenue_by_region.sql
│   ├── 06_customer_segment_analysis.sql
│   ├── 07_discount_analysis.sql
│   ├── 08_sales_channel_analysis.sql
│   └── 09_monthly_revenue_trend.sql
│
├── src/
│   ├── data_generator.py
│   ├── database_loader.py
│   ├── data_quality.py
│   ├── data_cleaning.py
│   └── pandas_analysis.py
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

# 📌 Features

## Data Generation

- Generate synthetic retail datasets
- Customers
- Products
- Orders
- Order Items
- Deliveries
- Returns

---

## Database

- SQLite database
- Relational schema
- Automated database loading

---

## Data Quality

- Missing value detection
- Duplicate detection
- Data validation
- Data quality report generation

---

## Data Cleaning

- Remove duplicates
- Clean invalid records
- Export processed datasets

---

## SQL Business Analysis

The project answers important business questions using SQL.

- Total Revenue
- Top Revenue Products
- Revenue by Category
- Revenue by Region
- Customer Segment Analysis
- Discount Analysis
- Sales Channel Analysis
- Monthly Revenue Trend

---

## Pandas Business Analysis

The same business questions are answered using Pandas.

- Total Revenue
- Top Revenue Products
- Revenue by Region
- Customer Segment Analysis
- Discount Analysis
- Sales Channel Analysis
- Monthly Revenue Trend

---

## Automated Reports

The project automatically generates business reports inside the **reports/** folder.

Examples include:

- Revenue by Region
- Revenue by Segment
- Discount Analysis
- Sales Channel Analysis
- Monthly Revenue Trend
- Top Products

---

# 📈 Business Insights Generated

The project helps identify:

- High revenue-generating products
- Best-performing customer segments
- Regional sales performance
- Sales channel effectiveness
- Discount impact on revenue
- Monthly business growth trends
- Revenue leak opportunities

---

# ▶️ How to Run

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/Revenue-Leak-Growth-Opportunity-Analyzer.git

cd Revenue-Leak-Growth-Opportunity-Analyzer
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Generate Raw Data

```bash
python src/data_generator.py
```

---

## 4. Load Data into SQLite

```bash
python src/database_loader.py
```

---

## 5. Run Data Quality Checks

```bash
python src/data_quality.py
```

---

## 6. Clean the Data

```bash
python src/data_cleaning.py
```

---

## 7. Run Pandas Analysis

```bash
python src/pandas_analysis.py
```

---

# 📷 Screenshots

Add screenshots of:

- Project Structure
- SQLite Database
- SQL Query Results
- Pandas Analysis Output
- Generated Reports

---

# 🎯 Skills Demonstrated

- Business Analytics
- Data Cleaning
- ETL Pipeline
- SQL
- SQLite
- Python
- Pandas
- Data Manipulation
- Report Generation
- Business Insight Extraction
- Problem Solving

---

# 🚀 Future Improvements

Possible future enhancements include:

- Interactive Power BI Dashboard
- Excel Dashboard
- Predictive Sales Forecasting
- Customer Churn Analysis
- Profit Margin Analysis
- KPI Dashboard
- Streamlit Web Application

---

# 👨‍💻 Author

**Biswajeet Ojha**

Aspiring Business Analyst passionate about transforming raw data into actionable business insights using SQL, Python, and Pandas.

GitHub:
https://github.com/your-username

LinkedIn:
https://linkedin.com/in/your-linkedin

---

# ⭐ If you found this project useful, consider giving it a Star!