import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")
# Compute average sale price for each quality level
quality_avg_price = df.groupby("OverallQual")["SalePrice"].mean()

# Plot bar chart
plt.figure(figsize=(10, 5))
plt.bar(quality_avg_price.index, quality_avg_price.values, color="skyblue", edgecolor="black")

plt.xlabel("Overall Quality")
plt.ylabel("Average Sale Price")
plt.title("Average Sale Price by Overall Quality")

# Show plot
plt.show()
