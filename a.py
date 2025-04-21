import pandas as pd
import matplotlib.pyplot as plt

# Load your cleaned dataset
df = pd.read_csv("sales_data_cleaned.csv")

# Convert orderdate column to datetime if it's not already
df['orderdate'] = pd.to_datetime(df['orderdate'])

# Group by month and sum the sales
monthly_sales = df.groupby(df['orderdate'].dt.to_period("M"))['sales'].sum().sort_index()

# Convert period to timestamp for plotting
monthly_sales.index = monthly_sales.index.to_timestamp()

# Plotting the results
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o', linestyle='-')
plt.title("Total Sales Over Time", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Total Sales", fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#This code for data visualisation accordingly
