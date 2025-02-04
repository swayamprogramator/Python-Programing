import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("rainfall_data.csv")

# Assign colors based on rainfall amount
colors = plt.cm.coolwarm(df["Rainfall (mm)"] / max(df["Rainfall (mm)"]))

# Create subplots: 1 row, 3 columns
fig, axs = plt.subplots(1, 3, figsize=(20, 5))

# Plot bar chart
axs[0].bar(df["Month"], df["Rainfall (mm)"], color=colors, edgecolor="black")
axs[0].set_xlabel("Month")
axs[0].set_ylabel("Rainfall (mm)")
axs[0].set_title("Monthly Rainfall using 'coolwarm' Color Scale")

# Plot histogram
axs[1].hist(df["Rainfall (mm)"], bins=10, color=plt.cm.viridis(0.6), edgecolor="black")
axs[1].set_xlabel("Rainfall (mm)")
axs[1].set_ylabel("Frequency")
axs[1].set_title("Rainfall Distribution using 'viridis' Color Scale")

# Scatter plot for Rainfall vs Temperature
scatter = axs[2].scatter(df["Temperature (°C)"], df["Rainfall (mm)"], c=df["Rainfall (mm)"], cmap="plasma", edgecolor="black")
axs[2].set_xlabel("Temperature (°C)")
axs[2].set_ylabel("Rainfall (mm)")
axs[2].set_title("Rainfall vs Temperature using 'plasma' Color Scale")

# Add colorbar for the scatter plot
fig.colorbar(scatter, ax=axs[2], label="Rainfall (mm)")

# Adjust layout
plt.tight_layout()
plt.show()
