import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("rainfall_data.csv")

# Display first few rows
print(df.head())

plt.figure(figsize=(10, 5))
plt.bar(df["Month"], df["Rainfall (mm)"], color="skyblue", edgecolor="black")

# Labels and title
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.title("Monthly Rainfall (Vertical Bar Plot)")

plt.figure(figsize=(10, 5))
plt.barh(df["Month"], df["Rainfall (mm)"], color="lightcoral", edgecolor="black")

# Labels and title
plt.xlabel("Rainfall (mm)")
plt.ylabel("Month")
plt.title("Monthly Rainfall (Horizontal Bar Plot)")

# Show plot
plt.show()


import numpy as np

x = np.arange(len(df["Month"]))  # X-axis positions
width = 0.4  # Width of bars

plt.figure(figsize=(10, 5))
plt.bar(x - width/2, df["Rainfall (mm)"], width, label="Rainfall (mm)", color="royalblue")
plt.bar(x + width/2, df["Temperature (°C)"], width, label="Temperature (°C)", color="orange")

# Labels and title
plt.xlabel("Month")
plt.ylabel("Values")
plt.title("Rainfall & Temperature (Grouped Bar Plot)")
plt.xticks(x, df["Month"])  # Set month labels
plt.legend()  # Add legend

# Show plot
plt.show()


plt.figure(figsize=(10, 5))
plt.bar(df["Month"], df["Rainfall (mm)"], label="Rainfall (mm)", color="mediumseagreen")
plt.bar(df["Month"], df["Temperature (°C)"], label="Temperature (°C)", color="gold", bottom=df["Rainfall (mm)"])

# Labels and title
plt.xlabel("Month")
plt.ylabel("Values")
plt.title("Rainfall & Temperature (Stacked Bar Plot)")
plt.legend()

# Show plot
plt.show()


# Show plot
plt.show()
