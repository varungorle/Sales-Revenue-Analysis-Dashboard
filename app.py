import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("ecommerce_behavior.csv")

df.dropna(inplace=True)

# =========================
# SIDEBAR FILTERS (SLICERS)
# =========================
st.sidebar.title("Filters")

city_filter = st.sidebar.multiselect(
    "Select City",
    df["City"].unique(),
    default=df["City"].unique()
)

membership_filter = st.sidebar.multiselect(
    "Select Membership Type",
    df["Membership Type"].unique(),
    default=df["Membership Type"].unique()
)

gender_filter = st.sidebar.multiselect(
    "Select Gender",
    df["Gender"].unique(),
    default=df["Gender"].unique()
)

# Apply filters
filtered_df = df[
    (df["City"].isin(city_filter)) &
    (df["Membership Type"].isin(membership_filter)) &
    (df["Gender"].isin(gender_filter))
]

# =========================
# TITLE
# =========================
st.title("📊 Customer Behavior & Revenue Dashboard")

# =========================
# KPI CARDS
# =========================
st.metric("Total Customers", filtered_df["Customer ID"].nunique())
st.metric("Total Revenue", round(filtered_df["Total Spend"].sum(), 2))
st.metric("Average Rating", round(filtered_df["Average Rating"].mean(), 2))

# =========================
# CHART 1: CITY SALES
# =========================
st.subheader("Revenue by City")

city_sales = filtered_df.groupby("City")["Total Spend"].sum()

fig1, ax1 = plt.subplots()
city_sales.plot(kind="bar", ax=ax1)
st.pyplot(fig1)

# =========================
# CHART 2: MEMBERSHIP
# =========================
st.subheader("Revenue by Membership Type")

membership_sales = filtered_df.groupby("Membership Type")["Total Spend"].sum()

fig2, ax2 = plt.subplots()
membership_sales.plot(kind="pie", autopct="%1.1f%%", ax=ax2)
ax2.set_ylabel("")
st.pyplot(fig2)

# =========================
# CHART 3: AGE vs SPENDING
# =========================
st.subheader("Age vs Spending")

fig3, ax3 = plt.subplots()
ax3.scatter(filtered_df["Age"], filtered_df["Total Spend"])
ax3.set_xlabel("Age")
ax3.set_ylabel("Total Spend")
st.pyplot(fig3)

# =========================
# CHART 4: SATISFACTION
# =========================
st.subheader("Customer Satisfaction")

satisfaction = filtered_df["Satisfaction Level"].value_counts()

fig4, ax4 = plt.subplots()
satisfaction.plot(kind="bar", ax=ax4)
st.pyplot(fig4)

# =========================
# INSIGHTS
# =========================
st.subheader("Key Insights")

st.write("""
- Revenue changes based on city and membership type
- Gold members contribute the highest spending
- Age group affects purchasing behavior
- Customer satisfaction is mostly positive for high spenders
""")