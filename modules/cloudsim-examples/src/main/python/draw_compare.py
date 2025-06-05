import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def draw_compare(file_name):
    task_nums = 100
    vm_nums = 3
    iteration_nums = 10

    

    # Read data from CSV file
    df1 = pd.read_csv(f"modules/cloudsim-examples/src/main/python/Synthetic_{task_nums}_{vm_nums}_{iteration_nums}" + f"/{file_name}")
    df2 = pd.read_csv(f"modules/cloudsim-examples/src/main/python/Random_{task_nums}_{vm_nums}_{iteration_nums}" + f"/{file_name}")
    df3 = pd.read_csv(f"modules/cloudsim-examples/src/main/python/GoCJ_{task_nums}_{vm_nums}_{iteration_nums}" + f"/{file_name}")

    print(df1)
    metrics = ["Makespan", "TotalCost", "Utilization", "Imbalance"]
    


    for i in range(len(metrics)):

        # Plot the distribution with side-by-side bars
        bar_width = 0.3
        index = np.arange(3)
        color1 = (223/255, 122/255, 94/255)
        color2 = (60/255, 64/255, 91/255)
        color3 = (130/255, 178/255, 154/255)
        
        metric = metrics[i]
        plt.figure(figsize=(10, 8), dpi=300)
        # plt.rcParams.update({'font.weight': 'bold', 'axes.labelweight': 'bold', 'axes.titleweight': 'bold'})
        bars1 = plt.bar(index, df1[metric], bar_width, label="Synthetic", color=color3)
        bars2 = plt.bar(index + bar_width, df2[metric], bar_width, label="Random", color=color2)
        bars3 = plt.bar(index + 2*bar_width, df3[metric], bar_width, label="GoCJ", color=color1)


        # Add data labels
        for bar in bars1:
            height = bar.get_height()
            if height !=0:
                plt.text(bar.get_x() + bar.get_width() / 2, height, f"{round(height, 2)}", ha='center', va='bottom', fontsize=22)

        for bar in bars2:
            height = bar.get_height()
            if height !=0:
                plt.text(bar.get_x() + bar.get_width() / 2, height, f"{round(height, 2)}", ha='center', va='bottom', fontsize=22)

        for bar in bars3:
            height = bar.get_height()
            if height !=0:
                plt.text(bar.get_x() + bar.get_width() / 2, height, f"{round(height, 2)}", ha='center', va='bottom', fontsize=22)

        plt.legend(fontsize=24)
        plt.xlabel("Algorithms", fontsize=32)
        plt.ylabel(f"{metric}", fontsize=32)
        plt.xticks(index + bar_width / 2, df1['Algo'], fontsize=24)
        plt.yticks(fontsize=24)
        plt.tight_layout()

        plt.savefig(f"modules/cloudsim-examples/src/main/python/figs/result_figs/{metric}_result_compare_{task_nums}.pdf")
        # plt.show()
    

if __name__ == '__main__':
    draw_compare("compare.csv")