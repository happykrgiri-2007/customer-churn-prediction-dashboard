import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Customer Churn Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# HTML IS USED ONLY FOR STYLING
# ============================================================

st.markdown(
    """
<style>

/* ============================================================
   APPLICATION BACKGROUND
   ============================================================ */

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(37, 99, 235, 0.15),
            transparent 28%
        ),
        radial-gradient(
            circle at 90% 10%,
            rgba(124, 58, 237, 0.13),
            transparent 28%
        ),
        linear-gradient(
            135deg,
            #07111f 0%,
            #0b1628 50%,
            #101827 100%
        );
}


/* ============================================================
   MAIN CONTENT
   ============================================================ */

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ============================================================
   TEXT COLORS
   ============================================================ */

h1 {
    color: #ffffff !important;
}

h2 {
    color: #ffffff !important;
}

h3 {
    color: #f8fafc !important;
}

h4 {
    color: #f8fafc !important;
}

p {
    color: #cbd5e1 !important;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #06101d 0%,
            #0b1728 100%
        );

    border-right: 1px solid rgba(148, 163, 184, 0.15);
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #ffffff !important;
}

section[data-testid="stSidebar"] p {
    color: #94a3b8 !important;
}

section[data-testid="stSidebar"] label {
    color: #cbd5e1 !important;
}


/* ============================================================
   KPI CARDS
   ============================================================ */

div[data-testid="metric-container"] {
    background:
        linear-gradient(
            145deg,
            rgba(30, 41, 59, 0.95),
            rgba(15, 23, 42, 0.98)
        );

    border: 1px solid rgba(148, 163, 184, 0.18);

    border-radius: 18px;

    padding: 20px;

    box-shadow:
        0 10px 30px rgba(0, 0, 0, 0.25);
}

div[data-testid="stMetricLabel"] {
    color: #94a3b8 !important;
}

div[data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-weight: 800 !important;
}


/* ============================================================
   FILTER BOXES
   ============================================================ */

div[data-baseweb="select"] > div {
    border-radius: 10px;
}


/* ============================================================
   INSIGHT CONTAINERS
   ============================================================ */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background:
        linear-gradient(
            145deg,
            rgba(30, 41, 59, 0.92),
            rgba(15, 23, 42, 0.97)
        );

    border: 1px solid rgba(148, 163, 184, 0.16);

    border-radius: 18px;

    box-shadow:
        0 8px 25px rgba(0, 0, 0, 0.20);
}


/* ============================================================
   ALERT / INFO BOXES
   ============================================================ */

div[data-testid="stAlert"] {
    border-radius: 12px;
}


/* ============================================================
   DIVIDER
   ============================================================ */

hr {
    border-color: rgba(148, 163, 184, 0.15) !important;
}


/* ============================================================
   CAPTION
   ============================================================ */

div[data-testid="stCaptionContainer"] {
    color: #94a3b8 !important;
}

</style>
""",
    unsafe_allow_html=True
)

# ============================================================
# LOAD DATASET
# ============================================================

@st.cache_data
def load_data():

    data = pd.read_csv("Dataset.csv")

    # Convert numeric columns
    data["tenure"] = pd.to_numeric(
        data["tenure"],
        errors="coerce"
    )

    data["MonthlyCharges"] = pd.to_numeric(
        data["MonthlyCharges"],
        errors="coerce"
    )

    data["TotalCharges"] = pd.to_numeric(
        data["TotalCharges"],
        errors="coerce"
    )

    # Clean text columns
    text_columns = [
        "gender",
        "Partner",
        "Dependents",
        "PhoneService",
        "MultipleLines",
        "InternetService",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
        "Contract",
        "PaperlessBilling",
        "PaymentMethod",
        "Churn"
    ]

    for column in text_columns:

        if column in data.columns:

            data[column] = (
                data[column]
                .astype(str)
                .str.strip()
            )

    # Remove rows missing essential analytical values
    data = data.dropna(
        subset=[
            "tenure",
            "MonthlyCharges",
            "TotalCharges",
            "Churn"
        ]
    )

    return data


df = load_data()

# ============================================================
# DASHBOARD HEADER
# ============================================================

st.title("📊 Customer Churn Intelligence")

st.write(
    "Interactive analytics dashboard for understanding "
    "customer churn, retention patterns and business opportunities."
)

st.caption(
    "DIGITAL KUPPAM  •  DATA SCIENCE INTERNSHIP  •  TASK 2"
)

st.divider()

# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.title("🔎 Filter & Segmentation")

st.sidebar.write(
    "Use the filters below to explore different customer segments."
)

st.sidebar.divider()

# ============================================================
# GENDER FILTER
# ============================================================

gender_options = sorted(
    df["gender"].dropna().unique()
)

selected_gender = st.sidebar.multiselect(
    "Gender",
    options=gender_options,
    default=gender_options
)

# ============================================================
# SENIOR CITIZEN FILTER
# ============================================================

senior_options = sorted(
    df["SeniorCitizen"].dropna().unique()
)

selected_senior = st.sidebar.multiselect(
    "Senior Citizen",
    options=senior_options,
    default=senior_options,
    format_func=lambda x: "Yes" if x == 1 else "No"
)

# ============================================================
# PARTNER FILTER
# ============================================================

partner_options = sorted(
    df["Partner"].dropna().unique()
)

selected_partner = st.sidebar.multiselect(
    "Partner",
    options=partner_options,
    default=partner_options
)

# ============================================================
# CONTRACT FILTER
# ============================================================

contract_options = sorted(
    df["Contract"].dropna().unique()
)

selected_contract = st.sidebar.multiselect(
    "Contract Type",
    options=contract_options,
    default=contract_options
)

# ============================================================
# INTERNET SERVICE FILTER
# ============================================================

internet_options = sorted(
    df["InternetService"].dropna().unique()
)

selected_internet = st.sidebar.multiselect(
    "Internet Service",
    options=internet_options,
    default=internet_options
)

# ============================================================
# PAYMENT METHOD FILTER
# ============================================================

payment_options = sorted(
    df["PaymentMethod"].dropna().unique()
)

selected_payment = st.sidebar.multiselect(
    "Payment Method",
    options=payment_options,
    default=payment_options
)

# ============================================================
# RESET FILTER BUTTON
# ============================================================

st.sidebar.divider()

st.sidebar.caption(
    "💡 Tip: Change the filters to analyze specific customer segments."
)

# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df[
    (df["gender"].isin(selected_gender))
    &
    (df["SeniorCitizen"].isin(selected_senior))
    &
    (df["Partner"].isin(selected_partner))
    &
    (df["Contract"].isin(selected_contract))
    &
    (df["InternetService"].isin(selected_internet))
    &
    (df["PaymentMethod"].isin(selected_payment))
]

# ============================================================
# CHECK FOR EMPTY DATA
# ============================================================

if filtered_df.empty:

    st.warning(
        "⚠️ No customers match the selected filters. "
        "Please change your filter selections."
    )

    st.stop()

# ============================================================
# KPI CALCULATIONS
# ============================================================

total_customers = len(filtered_df)

churned_customers = (
    filtered_df["Churn"]
    .astype(str)
    .str.strip()
    .str.lower()
    .eq("yes")
    .sum()
)

churn_rate = (
    churned_customers /
    total_customers *
    100
)

average_tenure = (
    filtered_df["tenure"].mean()
)

average_monthly_charges = (
    filtered_df["MonthlyCharges"].mean()
)

# ============================================================
# KEY PERFORMANCE INDICATORS
# ============================================================

st.subheader("📌 Key Performance Indicators")

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        label="👥 Total Customers",
        value=f"{total_customers:,}"
    )

with k2:

    st.metric(
        label="📉 Churn Rate",
        value=f"{churn_rate:.2f}%"
    )

with k3:

    st.metric(
        label="⏱️ Average Tenure",
        value=f"{average_tenure:.1f} months"
    )

with k4:

    st.metric(
        label="💰 Avg Monthly Charges",
        value=f"{average_monthly_charges:.2f}"
    )

st.divider()

# ============================================================
# CHURN ANALYSIS
# ============================================================

st.subheader("📈 Churn Analysis")

# ============================================================
# CONTRACT CHURN
# ============================================================

contract_data = (
    filtered_df
    .groupby("Contract")["Churn"]
    .apply(
        lambda x:
        x.astype(str)
        .str.strip()
        .str.lower()
        .eq("yes")
        .mean() * 100
    )
    .reset_index(name="Churn Rate")
)

# ============================================================
# PAYMENT METHOD CHURN
# ============================================================

payment_data = (
    filtered_df
    .groupby("PaymentMethod")["Churn"]
    .apply(
        lambda x:
        x.astype(str)
        .str.strip()
        .str.lower()
        .eq("yes")
        .mean() * 100
    )
    .reset_index(name="Churn Rate")
)

# ============================================================
# CONTRACT + PAYMENT CHARTS
# ============================================================

chart1, chart2 = st.columns(2)

# ============================================================
# CONTRACT CHART
# ============================================================

with chart1:

    st.markdown("### 📄 Churn by Contract Type")

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    sns.barplot(
        data=contract_data,
        x="Contract",
        y="Churn Rate",
        ax=ax
    )

    ax.set_title(
        "Churn Rate by Contract Type",
        fontsize=14,
        fontweight="bold"
    )

    ax.set_xlabel("Contract Type")
    ax.set_ylabel("Churn Rate (%)")

    for container in ax.containers:

        ax.bar_label(
            container,
            fmt="%.1f%%",
            padding=3
        )

    plt.xticks(rotation=15)

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)

# ============================================================
# PAYMENT CHART
# ============================================================

with chart2:

    st.markdown("### 💳 Churn by Payment Method")

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    sns.barplot(
        data=payment_data,
        x="PaymentMethod",
        y="Churn Rate",
        ax=ax
    )

    ax.set_title(
        "Churn Rate by Payment Method",
        fontsize=14,
        fontweight="bold"
    )

    ax.set_xlabel("Payment Method")
    ax.set_ylabel("Churn Rate (%)")

    for container in ax.containers:

        ax.bar_label(
            container,
            fmt="%.1f%%",
            padding=3
        )

    plt.xticks(rotation=25)

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)

# ============================================================
# INTERNET SERVICE ANALYSIS
# ============================================================

internet_data = (
    filtered_df
    .groupby("InternetService")["Churn"]
    .apply(
        lambda x:
        x.astype(str)
        .str.strip()
        .str.lower()
        .eq("yes")
        .mean() * 100
    )
    .reset_index(name="Churn Rate")
)

# ============================================================
# GENDER DISTRIBUTION
# ============================================================

gender_data = (
    filtered_df["gender"]
    .value_counts()
)

# ============================================================
# INTERNET + GENDER
# ============================================================

chart3, chart4 = st.columns(2)

# ============================================================
# INTERNET SERVICE CHART
# ============================================================

with chart3:

    st.markdown("### 🌐 Churn by Internet Service")

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    sns.barplot(
        data=internet_data,
        x="InternetService",
        y="Churn Rate",
        ax=ax
    )

    ax.set_title(
        "Churn Rate by Internet Service",
        fontsize=14,
        fontweight="bold"
    )

    ax.set_xlabel("Internet Service")
    ax.set_ylabel("Churn Rate (%)")

    for container in ax.containers:

        ax.bar_label(
            container,
            fmt="%.1f%%",
            padding=3
        )

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)

# ============================================================
# GENDER PIE CHART
# ============================================================

with chart4:

    st.markdown("### 👤 Customer Distribution by Gender")

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    ax.pie(
        gender_data.values,
        labels=gender_data.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title(
        "Customer Distribution by Gender",
        fontsize=14,
        fontweight="bold"
    )

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)

# ============================================================
# ADDITIONAL ANALYSIS
# ============================================================

st.divider()

st.subheader("🔬 Additional Churn Analysis")

# ============================================================
# SENIOR CITIZEN ANALYSIS
# ============================================================

senior_data = (
    filtered_df
    .groupby("SeniorCitizen")["Churn"]
    .apply(
        lambda x:
        x.astype(str)
        .str.strip()
        .str.lower()
        .eq("yes")
        .mean() * 100
    )
    .reset_index(name="Churn Rate")
)

senior_data["SeniorCitizen"] = (
    senior_data["SeniorCitizen"]
    .map(
        {
            0: "Non-Senior Citizen",
            1: "Senior Citizen"
        }
    )
)

# ============================================================
# TENURE GROUP
# ============================================================

tenure_df = filtered_df.copy()

tenure_df["Tenure Group"] = pd.cut(
    tenure_df["tenure"],
    bins=[
        0,
        12,
        24,
        48,
        72
    ],
    labels=[
        "0–12 Months",
        "13–24 Months",
        "25–48 Months",
        "49–72 Months"
    ],
    include_lowest=True
)

tenure_data = (
    tenure_df
    .groupby(
        "Tenure Group",
        observed=False
    )["Churn"]
    .apply(
        lambda x:
        x.astype(str)
        .str.strip()
        .str.lower()
        .eq("yes")
        .mean() * 100
    )
    .reset_index(name="Churn Rate")
)

# ============================================================
# SENIOR + TENURE CHARTS
# ============================================================

chart5, chart6 = st.columns(2)

# ============================================================
# SENIOR CITIZEN CHART
# ============================================================

with chart5:

    st.markdown("### 👴 Churn by Senior Citizen Status")

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    sns.barplot(
        data=senior_data,
        x="SeniorCitizen",
        y="Churn Rate",
        ax=ax
    )

    ax.set_title(
        "Churn by Senior Citizen Status",
        fontsize=14,
        fontweight="bold"
    )

    ax.set_xlabel("")
    ax.set_ylabel("Churn Rate (%)")

    for container in ax.containers:

        ax.bar_label(
            container,
            fmt="%.1f%%",
            padding=3
        )

    plt.xticks(rotation=10)

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)

# ============================================================
# TENURE CHART
# ============================================================

with chart6:

    st.markdown("### ⏳ Churn Rate by Tenure Group")

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    sns.barplot(
        data=tenure_data,
        x="Tenure Group",
        y="Churn Rate",
        ax=ax
    )

    ax.set_title(
        "Churn Rate by Tenure Group",
        fontsize=14,
        fontweight="bold"
    )

    ax.set_xlabel("Tenure")
    ax.set_ylabel("Churn Rate (%)")

    for container in ax.containers:

        ax.bar_label(
            container,
            fmt="%.1f%%",
            padding=3
        )

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)

# ============================================================
# BUSINESS INSIGHTS
# ============================================================

st.divider()

st.subheader("💡 Business Insights & Recommendations")

# ============================================================
# FIND HIGHEST-RISK CATEGORIES
# ============================================================

highest_contract = contract_data.loc[
    contract_data["Churn Rate"].idxmax()
]

highest_payment = payment_data.loc[
    payment_data["Churn Rate"].idxmax()
]

highest_internet = internet_data.loc[
    internet_data["Churn Rate"].idxmax()
]

highest_tenure = tenure_data.loc[
    tenure_data["Churn Rate"].idxmax()
]

highest_senior = senior_data.loc[
    senior_data["Churn Rate"].idxmax()
]

# ============================================================
# INSIGHT 1
# ============================================================

with st.container(border=True):

    st.markdown("### 🔴 01 — Contract Risk")

    st.write(
        f"The **{highest_contract['Contract']}** contract category "
        f"has the highest churn rate at "
        f"**{highest_contract['Churn Rate']:.1f}%**."
    )

    st.info(
        "💡 Recommendation: Encourage customers to move toward "
        "longer-term contracts through loyalty rewards, discounts "
        "and targeted retention offers."
    )

# ============================================================
# INSIGHT 2
# ============================================================

with st.container(border=True):

    st.markdown("### 🟠 02 — Payment Method Risk")

    st.write(
        f"**{highest_payment['PaymentMethod']}** has the highest "
        f"churn rate among payment methods at "
        f"**{highest_payment['Churn Rate']:.1f}%**."
    )

    st.info(
        "💡 Recommendation: Review the payment experience and "
        "promote convenient automated payment options."
    )

# ============================================================
# INSIGHT 3
# ============================================================

with st.container(border=True):

    st.markdown("### 🟡 03 — Internet Service Risk")

    st.write(
        f"**{highest_internet['InternetService']}** customers show "
        f"the highest churn rate among internet service categories "
        f"at **{highest_internet['Churn Rate']:.1f}%**."
    )

    st.info(
        "💡 Recommendation: Investigate service quality, technical "
        "issues and customer satisfaction for this customer segment."
    )

# ============================================================
# INSIGHT 4
# ============================================================

with st.container(border=True):

    st.markdown("### 🔵 04 — Early Customer Retention")

    st.write(
        f"The **{highest_tenure['Tenure Group']}** customer group "
        f"has the highest churn rate at "
        f"**{highest_tenure['Churn Rate']:.1f}%**."
    )

    st.info(
        "💡 Recommendation: Introduce stronger onboarding, "
        "customer engagement and early-stage retention campaigns."
    )

# ============================================================
# INSIGHT 5
# ============================================================

with st.container(border=True):

    st.markdown("### 🟣 05 — Senior Customer Risk")

    st.write(
        f"**{highest_senior['SeniorCitizen']}** customers show "
        f"the higher churn rate at "
        f"**{highest_senior['Churn Rate']:.1f}%**."
    )

    st.info(
        "💡 Recommendation: Design personalized support, service "
        "assistance and retention programs for higher-risk customers."
    )


# EXECUTIVE SUMMARY


st.divider()

st.subheader("🎯 Executive Summary")

st.success(
    f"""
    The selected customer segment contains **{total_customers:,} customers**
    with an overall churn rate of **{churn_rate:.2f}%**.

    The analysis identifies contract type, payment method, internet
    service, tenure and customer demographics as important dimensions
    for understanding customer churn and developing retention strategies.
    """
)


# FOOTER


st.divider()

st.caption(
    "📊 Customer Churn Intelligence Dashboard  |  "
    "Python • Pandas • Matplotlib • Seaborn • Streamlit  |  "
    "Digital Kuppam — Data Science Internship — Task 2"
)