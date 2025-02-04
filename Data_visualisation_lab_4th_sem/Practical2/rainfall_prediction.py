import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("rainfall_data.csv")
# Assign colors based on rainfall amount
colors = plt.cm.coolwarm(df["Rainfall (mm)"] / max(df["Rainfall (mm)"]))

# Plot bar chart
plt.figure(figsize=(10, 5))
plt.bar(df["Month"], df["Rainfall (mm)"], color=colors, edgecolor="black")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.title("Monthly Rainfall using 'coolwarm' Color Scale")
plt.show()

# Create a histogram
plt.figure(figsize=(10, 5))
plt.hist(df["Rainfall (mm)"], bins=10, color=plt.cm.viridis(0.6), edgecolor="black")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Frequency")
plt.title("Rainfall Distribution using 'viridis' Color Scale")
plt.show()

# Assume there is a "Temperature (°C)" column
plt.figure(figsize=(10, 5))
plt.scatter(df["Temperature (°C)"], df["Rainfall (mm)"], c=df["Rainfall (mm)"], cmap="plasma", edgecolor="black")
plt.colorbar(label="Rainfall (mm)")
plt.xlabel("Temperature (°C)")
plt.ylabel("Rainfall (mm)")
plt.title("Rainfall vs Temperature using 'plasma' Color Scale")
plt.show()


