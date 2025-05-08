import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# File paths for the two datasets
file1_path = 'modules\cloudsim-examples\src\main\java\scheduler\dataset\GoCJ\GoCJ_Dataset_1000.txt'
file2_path = 'modules\cloudsim-examples\src\main\java\scheduler\dataset\Synthetic\Synthetic_Dataset_1000.txt'

# Read the job sizes from both files
df1 = pd.read_csv(file1_path, header=None, names=["Job_Size"])
df2 = pd.read_csv(file2_path, header=None, names=["Job_Size"])

# Define the original and new job categories
original_categories = {
    "Small-Size": (15000, 55000),
    "Medium-Size": (59000, 99000),
    "Large-Size": (101000, 135000),
    "Extra-Large-Size": (150000, 337500),
    "Huge-Size": (525000, 900000)
}

new_categories = {
    "Tiny-Size": (1, 250),
    "Small-Size": (800, 1200),
    "Medium-Size": (1800, 2500),
    "Large-Size": (7000, 10000),
    "Extra-Large-Size": (30000, 45000)
}

# Categorize the jobs for each dataset
def categorize_job(size, categories):
    for category, (low, high) in categories.items():
        if low <= size <= high:
            return category
    return "Uncategorized"

df1["Category"] = df1["Job_Size"].apply(lambda x: categorize_job(x, original_categories))
df2["Category"] = df2["Job_Size"].apply(lambda x: categorize_job(x, new_categories))

# Count the number of jobs in each category
original_counts = df1["Category"].value_counts()
new_counts = df2["Category"].value_counts()


# Ensure all categories are present in the counts
all_categories = ["Tiny-Size", "Small-Size", "Medium-Size", "Large-Size", "Extra-Large-Size", "Huge-Size"]
original_counts = original_counts.reindex(all_categories, fill_value=0)
new_counts = new_counts.reindex(all_categories, fill_value=0)

# Plot the distribution with side-by-side bars
bar_width = 0.35
index = np.arange(len(all_categories))

plt.figure(figsize=(10, 8), dpi=300)
bars1 = plt.bar(index, original_counts.values, bar_width, label="GoCJ", color=(60/255,64/255,91/255))
bars2 = plt.bar(index + bar_width, new_counts.values, bar_width, label="Synthetic", color=(223/255,122/255,94/255))

# Add data labels
for bar in bars1:
    height = bar.get_height()
    if height !=0:
        plt.text(bar.get_x() + bar.get_width() / 2, height, f"{height}", ha='center', va='bottom', fontsize=20)

for bar in bars2:
    height = bar.get_height()
    if height !=0:
        plt.text(bar.get_x() + bar.get_width() / 2, height, f"{height}", ha='center', va='bottom', fontsize=20)

# plt.title("Cloudlet Size Distribution", fontsize=18)
plt.xlabel("Category", fontsize=28)
plt.ylabel("Number of Cloudlet", fontsize=28)
plt.xticks(index + bar_width / 2, all_categories, rotation=45, fontsize=24)
plt.yticks(fontsize=24)
plt.legend(loc="upper right", fontsize=22)
plt.tight_layout()
# plt.savefig("modules/cloudsim-examples/src/main/python/tasks_distribution_1000.eps")
plt.show()