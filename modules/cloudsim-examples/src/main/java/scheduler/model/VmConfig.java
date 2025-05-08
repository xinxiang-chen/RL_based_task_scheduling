package scheduler.model;


/**
 * @Author: Chen
 * @File Name: VmConfig.java
 */

public class VmConfig {
    public static final int VM_NUMS = 3;

//    // 每台 VM 的差异化配置
//    public static final int[] MIPS_LIST = {1000, 1500, 800};
//    public static final int[] PES_LIST = {1, 1, 1};
//    public static final int[] RAM_LIST = {2048, 4096, 1024};
//    public static final int[] BW_LIST = {10000, 20000, 5000};
//    public static final int[] SIZE_LIST = {100000, 150000, 80000};
//
//    // 每台 VM 的定制单位资源成本
//    public static final double[] COST_C1 = {0.001, 0.0008, 0.0015}; // CPU 时间权重
//    public static final double[] COST_C2 = {0.002, 0.001, 0.0025};  // 内存权重
//    public static final double[] COST_C3 = {0.001, 0.0005, 0.0015}; // 带宽权重
// 每台 VM 的差异化配置 (5台VM)
public static final int[] MIPS_LIST = {
        1000, 1500, 800,  // Original 3 VMs
        3000, 2500
};

    public static final int[] PES_LIST = {
            1, 1, 1,  // Original 3 VMs
            1, 1
    };

    public static final int[] RAM_LIST = {
            2048, 4096, 1024,  // Original 3 VMs
            4000, 3800
    };

    public static final int[] BW_LIST = {
            10000, 20000, 5000,  // Original 3 VMs
            9000, 8500
    };

    public static final int[] SIZE_LIST = {
            100000, 150000, 80000,  // Original 3 VMs
            140000, 130000
    };

    // 每台 VM 的定制单位资源成本 (MIPS 反比于成本)
// Original 3 VMs (unchanged)
    public static final double[] COST_C1 = {
            0.001, 0.0008, 0.0015,  // Original 3 VMs
            0.0003, 0.00035
    };

    public static final double[] COST_C2 = {
            0.002, 0.001, 0.0025,  // Original 3 VMs
            0.0005, 0.0006
    };

    public static final double[] COST_C3 = {
            0.001, 0.0005, 0.0015,  // Original 3 VMs
            0.0004, 0.00045
    };



    // 虚拟机管理器类型
    public static final String VMM = "Xen";
}
