# Import pandas library
import pandas as pd

# Step 1: Load the CSV file
df = pd.read_csv("sales_data.csv")

print("========== SALES DATA ANALYSIS ==========\n")

print("Dataset Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
# Numeric columns -> fill with 0
numeric_columns = df.select_dtypes(include="number").columns
df[numeric_columns] = df[numeric_columns].fillna(0)

# Text columns -> fill with "Unknown"
text_columns = df.select_dtypes(include="object").columns
df[text_columns] = df[text_columns].fillna("Unknown")

# Total Revenue
total_revenue = df["Total_Sales"].sum()

# Total Quantity Sold
total_quantity = df["Quantity"].sum()

# Average Sale
average_sale = df["Total_Sales"].mean()

# Best Selling Product (by quantity)
best_product = (
    df.groupby("Product")["Quantity"]
    .sum()
    .idxmax()
)

best_product_quantity = (
    df.groupby("Product")["Quantity"]
    .sum()
    .max()
)

# Revenue by Product
revenue_by_product = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== SALES REPORT ==========")

print(f"Total Revenue      : ₹{total_revenue:,.2f}")
print(f"Total Quantity Sold: {total_quantity}")
print(f"Average Sale Value : ₹{average_sale:,.2f}")

print(f"\nBest Selling Product: {best_product}")
print(f"Units Sold: {best_product_quantity}")

print("\nRevenue by Product:")
print(revenue_by_product)

print("\n========== REPORT COMPLETE ==========")