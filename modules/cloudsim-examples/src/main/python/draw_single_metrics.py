import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

task_nums = 100
vm_nums = 3
iteration_nums = 10
outward=70 # 35 for 500, 70 for 100

df1 = pd.read_csv(f"modules/cloudsim-examples/src/main/python/Random_{task_nums}_{vm_nums}_{iteration_nums}/result.csv")
df2 = pd.read_csv(f"modules/cloudsim-examples/src/main/python/GoCJ_{task_nums}_{vm_nums}_{iteration_nums}/result.csv")
df3 = pd.read_csv(f"modules/cloudsim-examples/src/main/python/Synthetic_{task_nums}_{vm_nums}_{iteration_nums}/result.csv")

# Set the metrics and colors
metrics = ["Makespan", "TotalCost", "Utilization", "Imbalance"]
color1 = (223/255, 122/255, 94/255)
color2 = (60/255, 64/255, 91/255)
color3 = (132/255, 178/255, 154/255)

plt.rcParams['lines.linewidth'] = 4
# plt.rcParams.update({'font.weight': 'bold', 'axes.labelweight': 'bold', 'axes.titleweight': 'bold'})


# Generate separate plots for each metric
for i, metric in enumerate(metrics):
    fig, ax1 = plt.subplots(figsize=(8,6))




    if i < 2:
        ax1.plot(df2["Iteration"], df2[metric], label="GoCJ", marker='o', color=color1, markersize=10)
        ax1.set_ylabel(f"{metric}", fontsize=32)
        ax1.tick_params(axis='y', labelsize=32)
        ax1.yaxis.set_major_formatter(ScalarFormatter())
        ax1.yaxis.get_major_formatter().set_scientific(True)
        ax1.yaxis.get_major_formatter().set_powerlimits((0, 0))
        ax1.yaxis.offsetText.set_fontsize(32)
        ax1.grid(True)




        # Secondary axis for Random
        ax2 = ax1.twinx()
        ax2.plot(df1["Iteration"], df1[metric], label="Random", marker='o', color=color2, markersize=10)

        ax2.tick_params(axis='y', colors=color2, labelsize=32)
        ax2.yaxis.set_major_formatter(ScalarFormatter())
        ax2.yaxis.get_major_formatter().set_scientific(True)
        ax2.yaxis.get_major_formatter().set_powerlimits((0, 0))
        ax2.yaxis.offsetText.set_fontsize(32)
        ax2.yaxis.set_visible(False)


        # Tertiary axis for Synthetic
        ax3 = ax1.twinx()
        ax3.spines["right"].set_position(("outward", outward))
        ax3.plot(df3["Iteration"], df3[metric], label="Synthetic", marker='o', color=color3, markersize=10)

        ax3.tick_params(axis='y', colors=color3, labelsize=32)
        ax3.yaxis.set_major_formatter(ScalarFormatter())
        ax3.yaxis.get_major_formatter().set_scientific(True)
        ax3.yaxis.get_major_formatter().set_powerlimits((0, 0))
        ax3.yaxis.offsetText.set_fontsize(32)
        ax3.yaxis.offsetText.set_position((1.25, 1.07))  # (x, y) in axis coordinates
        ax3.yaxis.set_visible(False)


        # Combine legends from all axes
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        lines3, labels3 = ax3.get_legend_handles_labels()
        ax1.legend(lines1 + lines2 + lines3, labels1 + labels2 + labels3, fontsize=22, loc='upper right')
    else:
        # Primary axis for GoCJ
        ax1.plot(df2["Iteration"], df2[metric], label="GoCJ", marker='o', color=color1, markersize=10)
        ax1.set_ylabel(f"{metric}", fontsize=32)
        ax1.plot(df1["Iteration"], df1[metric], label="Random", marker='o', color=color2, markersize=10)
        # ax1.set_ylabel(f"{metric} (GoCJ)", fontsize=24, color=color1)
        ax1.tick_params(axis='y', labelsize=32)

        ax1.plot(df3["Iteration"], df3[metric], label="Synthetic", marker='o', color=color3, markersize=10)
        # ax1.set_ylabel(f"{metric} (Synthetic)", fontsize=24, color=color1)
        ax1.tick_params(axis='y', labelsize=32)
        ax1.legend(fontsize=22)

    # Title and axis labels
    # plt.title(f"{metric} vs Iteration", fontsize=32)
    ax1.xaxis.set_major_formatter(ScalarFormatter())
    ax1.xaxis.get_major_formatter().set_scientific(True)
    ax1.xaxis.get_major_formatter().set_powerlimits((0, 0))
    ax1.xaxis.offsetText.set_fontsize(32)
    ax1.set_xlabel("Iteration", fontsize=32)
    ax1.tick_params(axis='x', labelsize=32)
    plt.grid(True)

    # Save each graph as a separate file
    plt.tight_layout(pad=2.0)
    plt.savefig(f"modules/cloudsim-examples/src/main/python/figs/result_figs/{metric}_exp_results_{task_nums}.pdf")
    # plt.show()
