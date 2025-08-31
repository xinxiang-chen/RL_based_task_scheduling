# Runtime Environment
1. All code is located in the `modules\cloudsim-examples\src\main` directory, while other code belongs to the CloudSim module;

2. To start the experiment: first `run rl_server.py`, and once the port is successfully listening, then start `Main.java`;

3. All experiment parameters (such as VM parameters, datasets, etc.) can be modified in the configuration files under `modules\cloudsim-examples\src\main\java\scheduler\model`;

4. After the experiment ends, both the model and the results will be saved in the `python\` directory, with the folder named as `dataset_taskNumber_vmNumber_iterations`;

5. Different simulation methods can be executed by running `Example.run()` in `Main.java`;

6. The `python` directory also contains some plotting code, but certain data needs to be manually collected and organized.

---
# 运行环境

1. 所有代码均在`modules\cloudsim-examples\src\main`目录下，其他代码为CloudSim模块代码；

2. 开始实验：首先启用`rl_server.py`，成功监听端口后再启动`Main.java`；

3. 所有的实验参数（虚拟机参数、数据集等）可以在`modules\cloudsim-examples\src\main\java\scheduler\model`目录下的配置文件中修改；

4. 实验结束后会分别保存模型和实验结果到`python\`目录下，文件夹命名为`数据集_任务数量_虚拟机数量_迭代次数`；

5. 通过在`Main.java`中运行不同的`Example.run()`来实现使用不同方法来模拟；

6. `python`目录下还包括一些画图代码，但是一些数据需要手动收集整理。
