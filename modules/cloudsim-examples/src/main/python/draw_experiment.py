import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

task_nums = 500
vm_nums = 5
iteration_nums = 10

df1 = pd.read_csv(f"modules/cloudsim-examples/src/main/python/Random_{task_nums}_{vm_nums}_{iteration_nums}/result.csv")
df2 = pd.read_csv(f"modules/cloudsim-examples/src/main/python/GoCJ_{task_nums}_{vm_nums}_{iteration_nums}/result.csv")
df3 = pd.read_csv(f"modules/cloudsim-examples/src/main/python/Synthetic_{task_nums}_{vm_nums}_{iteration_nums}/result.csv")

# 设置每个指标的折线图
metrics = ["Makespan", "TotalCost", "Utilization", "Imbalance"]

# 创建子图
fig, axes = plt.subplots(2, 2, figsize=(18, 12))  # 2x2 格局的子图
axes = axes.flatten()
color1 = (223/255,  122/255, 94/255)
color2 = (60/255,  64/255, 91/255)
color3 = (130/255,  178/255, 154/255)


plt.rcParams['lines.linewidth'] = 2.5

# 为每个指标创建单独的折线图
for i, metric in enumerate(metrics):
    if i < 2:
        # Primary axis
        ax1 = axes[i]
        ax2 = ax1.twinx()  # Secondary axis (right)
        
        # Third (invisible) axis
        ax3 = ax1.twinx()
        ax3.spines["right"].set_position(("outward", 80))  # Move the third axis to the right
        ax3.spines["right"].set_visible(True)  # Make it visible

        # Plot data
        ax1.plot(df2["Iteration"], df2[metric], label="GoCJ", marker='o', color=color1)
        ax2.plot(df1["Iteration"], df1[metric], label="Random", marker='o', color=color2)
        ax3.plot(df3["Iteration"], df3[metric], label="Synthetic", marker='o', color=color3)

        # Set labels and ticks
        ax1.set_ylabel(f"{metric} (GoCJ)", fontsize=24, color=color1)
        ax2.set_ylabel(f"{metric} (Random)", fontsize=24, color=color2)
        ax3.set_ylabel(f"{metric} (Synthetic)", fontsize=24, color=color3)
        
        # Set tick colors
        ax1.yaxis.set_major_formatter(ScalarFormatter())
        ax1.yaxis.get_major_formatter().set_scientific(True)
        ax1.yaxis.get_major_formatter().set_powerlimits((0, 0))
        ax2.yaxis.set_major_formatter(ScalarFormatter())
        ax2.yaxis.get_major_formatter().set_scientific(True)
        ax2.yaxis.get_major_formatter().set_powerlimits((0, 0))
        ax3.yaxis.set_major_formatter(ScalarFormatter())
        ax3.yaxis.get_major_formatter().set_scientific(True)
        ax3.yaxis.get_major_formatter().set_powerlimits((0, 0))


        ax1.tick_params(axis='y', colors=color1, labelsize=24)
        ax2.tick_params(axis='y', colors=color2, labelsize=24)
        ax3.tick_params(axis='y', colors=color3, labelsize=24)
        ax1.yaxis.offsetText.set_fontsize(24)
        ax2.yaxis.offsetText.set_fontsize(24)
        ax3.yaxis.offsetText.set_fontsize(24)
        axes[i].tick_params(axis='x', labelsize=24)


        # axes[i].text(0.5, -0.3, f"a {metrics[i]}", fontsize=20, ha='center', va='center', transform=axes[i].transAxes)

        # Combine legends
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        lines3, labels3 = ax3.get_legend_handles_labels()
        ax1.legend(lines1 + lines2 + lines3, labels1 + labels2 + labels3, fontsize=20, loc='upper right')

    else:
        # Plot without secondary or tertiary axes for the last two subplots
        axes[i].plot(df1["Iteration"], df1[metric], label="Random", marker='o', color=color1)
        axes[i].plot(df2["Iteration"], df2[metric], label="GoCJ", marker='o', color=color2)
        axes[i].plot(df3["Iteration"], df3[metric], label="Synthetic", marker='o', color=color3)
        axes[i].set_ylabel(metric, fontsize=24)
        axes[i].legend(fontsize=20)
        axes[i].tick_params(axis='y', labelsize=24)
        axes[i].tick_params(axis='x', labelsize=24)
        # axes[i].text(0.5, -0.3, f"a {metrics[i]}", fontsize=20, ha='center', va='center', transform=axes[i].transAxes)
    
    # Set title and x-axis labels
    # axes[i].set_title(f"{metric} vs Iteration", fontsize=14)
    axes[i].set_xlabel("Iteration", fontsize=24)
    axes[i].grid(True)




# 调整布局
# plt.subplots_adjust(hspace=0.3, wspace=0.3)
plt.tight_layout(pad=2.0, h_pad=3.0, w_pad=3.0)
plt.savefig(f"modules/cloudsim-examples/src/main/python/exp_results_{task_nums}.png")

# 显示图表
plt.show()
