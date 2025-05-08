package scheduler.env;


/**
 * @Author: Chen
 * @File Name: VmFactory.java
 */


import org.cloudbus.cloudsim.CloudletSchedulerSpaceShared;
import org.cloudbus.cloudsim.Vm;
import scheduler.model.VmConfig;

import java.util.ArrayList;
import java.util.List;

public class VmFactory {

    public static List<Vm> createVmList(int brokerId) {
        List<Vm> list = new ArrayList<>();

        int numVms = VmConfig.VM_NUMS;
        for (int i = 0; i < numVms; i++) {
            int idx = i % VmConfig.MIPS_LIST.length;
            Vm vm = new Vm(
                    i, brokerId,
                    VmConfig.MIPS_LIST[idx],
                    VmConfig.PES_LIST[idx],
                    VmConfig.RAM_LIST[idx],
                    VmConfig.BW_LIST[idx],
                    VmConfig.SIZE_LIST[idx],
                    VmConfig.VMM,
                    new CloudletSchedulerSpaceShared()  // 也可以传参切换策略
            );
            list.add(vm);
        }

        return list;
    }
}

