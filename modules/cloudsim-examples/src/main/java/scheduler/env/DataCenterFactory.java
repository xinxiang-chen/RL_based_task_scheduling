package scheduler.env;


/**
 * @Author: Chen
 * @File Name: DataCenterFactory.java
 */

import org.cloudbus.cloudsim.*;
import org.cloudbus.cloudsim.provisioners.BwProvisionerSimple;
import org.cloudbus.cloudsim.provisioners.PeProvisionerSimple;
import org.cloudbus.cloudsim.provisioners.RamProvisionerSimple;
import scheduler.model.HostConfig;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;


public class DataCenterFactory {

    public static Datacenter createSimpleDatacenter(String name) throws Exception {
        // 创建一个处理器列表
        List<Pe> peList = new ArrayList<>();
        List<Pe> peList1 = new ArrayList<>();
        List<Pe> peList2 = new ArrayList<>();
        List<Pe> peList3 = new ArrayList<>();
        List<Pe> peList4 = new ArrayList<>();
        for (int i = 0; i < HostConfig.NUM_PES; i++) {
            peList.add(new Pe(i, new PeProvisionerSimple(HostConfig.PE_MIPS)));
            peList1.add(new Pe(i, new PeProvisionerSimple(HostConfig.PE_MIPS)));
            peList2.add(new Pe(i, new PeProvisionerSimple(HostConfig.PE_MIPS)));
            peList3.add(new Pe(i, new PeProvisionerSimple(HostConfig.PE_MIPS)));
            peList4.add(new Pe(i, new PeProvisionerSimple(HostConfig.PE_MIPS)));
        }

        // 创建一个主机
        Host host = new Host(
                0,
                new RamProvisionerSimple(HostConfig.HOST_RAM),
                new BwProvisionerSimple(HostConfig.HOST_BW),
                HostConfig.HOST_STORAGE,
                peList,
                new VmSchedulerTimeShared(peList)
        );

        Host host1 = new Host(
                1,
                new RamProvisionerSimple(HostConfig.HOST_RAM),
                new BwProvisionerSimple(HostConfig.HOST_BW),
                HostConfig.HOST_STORAGE,
                peList1,
                new VmSchedulerTimeShared(peList1)
        );

        Host host2 = new Host(
                2,
                new RamProvisionerSimple(HostConfig.HOST_RAM),
                new BwProvisionerSimple(HostConfig.HOST_BW),
                HostConfig.HOST_STORAGE,
                peList2,
                new VmSchedulerTimeShared(peList2)
        );

        Host host3 = new Host(
                3,
                new RamProvisionerSimple(HostConfig.HOST_RAM),
                new BwProvisionerSimple(HostConfig.HOST_BW),
                HostConfig.HOST_STORAGE,
                peList3,
                new VmSchedulerTimeShared(peList3)
        );

        Host host4 = new Host(
                4,
                new RamProvisionerSimple(HostConfig.HOST_RAM),
                new BwProvisionerSimple(HostConfig.HOST_BW),
                HostConfig.HOST_STORAGE,
                peList4,
                new VmSchedulerTimeShared(peList4)
        );

        List<Host> hostList = new ArrayList<>();
        hostList.add(host);
//        hostList.add(host1);
//        hostList.add(host2);
//        hostList.add(host3);
//        hostList.add(host4);


        // 数据中心属性
        String arch = "x86";
        String os = "Linux";
        String vmm = "Xen";
        double timeZone = 10.0;
        double cost = 3.0;
        double costPerMem = 0.05;
        double costPerStorage = 0.001;
        double costPerBw = 0.0;

        DatacenterCharacteristics characteristics = new DatacenterCharacteristics(
                arch, os, vmm, hostList, timeZone,
                cost, costPerMem, costPerStorage, costPerBw
        );

        return new Datacenter(name, characteristics, new VmAllocationPolicySimple(hostList), new LinkedList<>(), 0);
    }
}

