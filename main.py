import polars as pl
import matplotlib.pyplot as plt

# Read the CSV 
sample_df = pl.read_csv("train.csv")

# Calculate summary 
summary = sample_df.describe()

# check first couple of rows
print(sample_df.head())

# Drop the 'id' and 'Population' columns
df_without_id = sample_df.drop(["id", "Population"])

columns = df_without_id.columns
data = [df_without_id[column].to_list() for column in columns]

plt.figure(figsize=(8, 6))
plt.boxplot(data, tick_labels=columns)
plt.title("Box and Whisker Plot (Excluding ID)")
plt.ylabel("Value")

# Save the box plot
plt.savefig("fig/sample2.png")

# Create a figure and axis for the summary table
fig, ax = plt.subplots(figsize=(10, 4))  # Adjust the size as necessary

# Hide the axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

summary_data = summary.to_numpy().tolist() 
column_labels = summary.columns
row_labels = summary.get_column(
    "statistic"
).to_list()  

# Create the table
table = ax.table(
    cellText=summary_data,
    colLabels=column_labels,
    rowLabels=row_labels,
    cellLoc="center",
    loc="center",
)

table.scale(1, 2)

# Save the plot with the table
plt.savefig("fig/summary.png")
