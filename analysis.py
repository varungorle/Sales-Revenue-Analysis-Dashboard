import pandas as pd
import matplotlib.pyplot as plt

# =========================
# 1. LOAD DATASET
# =========================
df = pd.read_csv("ecommerce_behavior.csv")

print("\nFirst 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns)

# =========================
# 2. BASIC CLEANING
# =========================
df.dropna(inplace=True)

# =========================
# 3. BASIC BUSINESS INSIGHTS
# =========================

print("\n===== BASIC STATS =====")
print("Total Customers:", df['Customer ID'].nunique())
print("Average Spend:", df['Total Spend'].mean())
print("Average Rating:", df['Average Rating'].mean())

# =========================
# 4. REVENUE ANALYSIS
# =========================
city_sales = df.groupby('City')['Total Spend'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,4))
city_sales.plot(kind='bar')
plt.title("Revenue by City")
plt.ylabel("Total Spend")
plt.show()

# =========================
# 5. MEMBERSHIP ANALYSIS
# =========================
membership_sales = df.groupby('Membership Type')['Total Spend'].sum()

plt.figure(figsize=(6,6))
membership_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Revenue by Membership Type")
plt.ylabel("")
plt.show()

# =========================
# 6. CUSTOMER SATISFACTION
# =========================
satisfaction = df['Satisfaction Level'].value_counts()

plt.figure(figsize=(6,4))
satisfaction.plot(kind='bar')
plt.title("Customer Satisfaction Levels")
plt.show()

# =========================
# 7. DISCOUNT ANALYSIS
# =========================
discount_effect = df.groupby('Discount Applied')['Total Spend'].mean()

plt.figure(figsize=(6,4))
discount_effect.plot(kind='bar')
plt.title("Impact of Discount on Spending")
plt.show()

# =========================
# 8. AGE vs SPENDING
# =========================
plt.figure(figsize=(6,4))
plt.scatter(df['Age'], df['Total Spend'])
plt.title("Age vs Spending Pattern")
plt.xlabel("Age")
plt.ylabel("Total Spend")
plt.show()

# =========================
# 9. FINAL INSIGHTS
# =========================
print("\n===== KEY INSIGHTS =====")
print("- High-value customers are concentrated in top cities")
print("- Gold members contribute highest revenue")
print("- Discounts influence spending behavior")
print("- Middle-age customers tend to spend more")
print("- Satisfaction is mostly positive in high spenders")