import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")
# Compute average sale price for each quality level
quality_avg_price = df.groupby("OverallQual")["SalePrice"].mean()

# Plot histogram of sale prices
plt.figure(figsize=(10, 5))
plt.hist(df["SalePrice"], bins=30, color="blue", edgecolor="black", alpha=0.7)

# Labels and title
plt.xlabel("Sale Price")
plt.ylabel("Frequency")
plt.title("Distribution of House Prices")

# Show plot
plt.show()
