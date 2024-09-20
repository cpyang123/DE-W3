import pandas as pd
import matplotlib.pyplot as plt


sample_df = pd.read_csv("train.csv")
summary = sample_df.describe()


# Refactor this into Functions

sample_df.head()

# Drop the 'ID' column before plotting
df_without_id = sample_df.drop(columns=["id", "Population"])

# Create a box plot for all columns in the dataframe excluding 'ID'
plt.figure(figsize=(8, 6))
df_without_id.boxplot()
plt.title("Box and Whisker Plot (Excluding ID)")
plt.ylabel("Value")

plt.savefig("fig/sample2.png")


# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 4))  # Adjust the size as necessary

# Hide the axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

# Create the table
table = ax.table(
    cellText=summary.values,
    colLabels=summary.columns,
    rowLabels=summary.index,
    cellLoc="center",
    loc="center",
)

# Adjust the table scale
table.scale(1, 2)

# Show the plot with the table
plt.savefig("fig/summary.png")
