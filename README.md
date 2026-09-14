# 📊 Customer Churn Intelligence Dashboard

An interactive **Customer Churn Analytics Dashboard** developed using Python, Pandas, Matplotlib, Seaborn, and Streamlit as part of the **Digital Kuppam Data Science Internship – Task 2**.

The dashboard helps analyze customer churn patterns, identify high-risk customer segments, and generate practical business recommendations for improving customer retention.

---

## 📌 Project Overview

Customer churn is a major challenge for telecom companies because losing existing customers can negatively affect revenue, customer lifetime value, and long-term business growth.

This project analyzes telecom customer data to understand churn behavior across different customer characteristics such as:

- Contract Type
- Payment Method
- Internet Service
- Technical Support
- Customer Tenure
- Senior Citizen Status
- Gender
- Monthly Charges

An interactive Streamlit dashboard has been developed to make the analysis easier to explore using filters, KPIs, visualizations, business insights, and recommendations.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Clean and prepare the customer churn dataset.
- Analyze customer churn patterns.
- Calculate important business KPIs.
- Visualize churn across different customer attributes.
- Provide interactive customer segmentation filters.
- Identify high-risk customer segments.
- Generate meaningful business insights.
- Provide actionable recommendations for customer retention.

---

## 📂 Dataset Description

The dataset contains telecom customer information with **7,043 customer records and 21 features**.

The dataset includes:

| Feature | Description |
|---|---|
| customerID | Unique customer identifier |
| gender | Customer gender |
| SeniorCitizen | Senior citizen status |
| Partner | Whether customer has a partner |
| Dependents | Whether customer has dependents |
| tenure | Number of months the customer has stayed |
| PhoneService | Phone service availability |
| MultipleLines | Multiple line service |
| InternetService | Type of internet service |
| OnlineSecurity | Online security service |
| OnlineBackup | Online backup service |
| DeviceProtection | Device protection service |
| TechSupport | Technical support service |
| StreamingTV | Streaming TV service |
| StreamingMovies | Streaming movies service |
| Contract | Contract type |
| PaperlessBilling | Paperless billing status |
| PaymentMethod | Payment method |
| MonthlyCharges | Monthly customer charges |
| TotalCharges | Total charges paid |
| Churn | Customer churn status |

### Dataset Summary

- **Total Customers:** 7,043
- **Total Features:** 21
- **Churned Customers:** 1,869
- **Overall Churn Rate:** 26.54%

---

## 🧹 Data Preparation

The following data preparation steps were performed:

1. Loaded the dataset using Pandas.
2. Converted `tenure` into numeric format.
3. Converted `MonthlyCharges` into numeric format.
4. Converted `TotalCharges` into numeric format.
5. Handled blank values in `TotalCharges`.
6. Filled the 11 missing `TotalCharges` values with `0`.
7. Cleaned whitespace from text-based columns.
8. Removed duplicate records.
9. Prepared the cleaned dataset for analysis and visualization.

The 11 customers with blank `TotalCharges` values were retained in the analysis by assigning their missing total charge value as `0`.

---

## 📊 Key Performance Indicators

The dashboard provides the following KPIs for the complete dataset:

| KPI | Value |
|---|---:|
| 👥 Total Customers | **7,043** |
| 📉 Churn Rate | **26.54%** |
| ⏱️ Average Tenure | **32.4 months** |
| 💰 Average Monthly Charges | **$64.76** |

---

## 🎛️ Interactive Filters

The dashboard provides interactive filters for customer segmentation.

Available filters include:

- Gender
- Senior Citizen
- Partner
- Contract Type
- Internet Service
-
