# Customer Churn Analytics Dashboard

An interactive Customer Churn Analytics Dashboard built using Python, Pandas, Plotly, and Streamlit.

The dashboard helps analyze customer churn patterns and provides business insights that can support customer retention strategies.

---

## 📌 Project Overview

Customer churn is a major challenge for telecom companies because losing existing customers can directly affect revenue and long-term growth.

This project analyzes customer information to identify churn patterns based on contract type, payment method, internet service, technical support, gender, tenure, and monthly charges.

An interactive Streamlit dashboard has been developed to make the analysis easy to explore and understand.

---

## 🎯 Objectives

- Analyze customer churn patterns.
- Clean and prepare the dataset.
- Calculate important business KPIs.
- Visualize churn across different customer attributes.
- Provide interactive filters for customer analysis.
- Identify major factors associated with customer churn.
- Provide actionable business recommendations.

---

## 📊 Dataset Description

The dataset contains telecom customer information including:

- Customer ID
- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Technical Support
- Streaming TV
- Streaming Movies
- Contract
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges
- Churn

### Dataset Size

- Total Customers: **7,043**
- Total Features: **21**

---

## 🧹 Data Preparation

The following preprocessing steps were performed:

- Converted `TotalCharges` into numeric format.
- Handled missing values in `TotalCharges`.
- Filled applicable missing `TotalCharges` values with 0.
- Checked and removed duplicate records.
- Prepared categorical variables for analysis.
- Created customer tenure groups for deeper analysis.
- Prepared the dataset for dashboard visualization.

---

## 📈 Key Metrics

The dashboard provides the following key metrics:

| Metric | Value |
|---|---:|
| Total Customers | 7,043 |
| Churned Customers | 1,869 |
| Churn Rate | 26.54% |
| Average Tenure | 32.37 months |
| Average Monthly Charges | $64.76 |

---

## 📊 Dashboard Visualizations

The dashboard includes:

- Churn by Contract Type
- Churn by Payment Method
- Churn by Internet Service
- Churn by Technical Support
- Customer Distribution by Gender
- Interactive customer filters
- Customer-level filtered data

---

## 🔍 Key Findings

### 1. Contract Type

Month-to-month customers have the highest churn rate:

- Month-to-month: **42.71%**
- One year: **11.27%**
- Two year: **2.83%**

This indicates that customers without long-term contracts are considerably more likely to leave.

### 2. Payment Method

Electronic check customers have the highest churn rate:

**45.29%**

Other payment methods have substantially lower churn rates.

### 3. Internet Service

Fiber optic customers show a relatively high churn rate:

**41.89%**

This suggests that pricing, service quality, or customer expectations may need further investigation.

### 4. Technical Support

Customers without technical support show a much higher churn rate than customers who have technical support.

### 5. Customer Tenure

New customers are more likely to churn.

Customers with 0–6 months of tenure have a churn rate of approximately:

**52.94%**

Customers with 49–72 months of tenure have a much lower churn rate of approximately:

**9.51%**

---

## 💡 Business Insights

1. Month-to-month customers are the highest-risk customer segment.
2. New customers have significantly higher churn risk.
3. Electronic check users show the highest churn rate among payment methods.
4. Customers without technical support are more likely to churn.
5. Fiber optic customers have comparatively high churn.
6. Customers with higher monthly charges show higher churn tendency.

---

## 🚀 Recommendations

### 1. Promote Long-Term Contracts

Offer discounts, loyalty benefits, and special incentives to encourage month-to-month customers to move to one-year or two-year contracts.

### 2. Improve New Customer Onboarding

Create a strong onboarding program during the first 6 months to improve customer satisfaction and reduce early churn.

### 3. Increase Technical Support Adoption

Promote technical support services and provide proactive assistance to customers experiencing service issues.

### 4. Encourage Automatic Payments

Provide incentives for customers to use automatic bank transfer or credit card payments.

### 5. Investigate Fiber Optic Churn

Analyze fiber optic pricing, service quality, technical issues, and customer expectations to identify the reasons behind higher churn.

---

## 🛠️ Technologies Used

- Python
- Pandas
- Plotly
- Streamlit
- GitHub

---

## 📁 Project Structure

```text
customer-churn-prediction-dashboard/
│
├── app.py
├── Dataset.csv
├── requirements.txt
├── README.md
│
└── report/
    └── Customer_Churn_Analytics_Task_2_Report_Final.pdf
