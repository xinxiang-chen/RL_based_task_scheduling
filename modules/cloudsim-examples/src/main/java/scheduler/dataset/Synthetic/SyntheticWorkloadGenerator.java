package scheduler.dataset.Synthetic;


/**
 * @Author: Chen
 * @File Name: SyntheticWorkloadGenerator.java
 */

import scheduler.model.CloudletConfig;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class SyntheticWorkloadGenerator {

    // Job size ranges in MIs
    private static final int TINY_MIN = 100;
    private static final int TINY_MAX = 250;
    private static final int SMALL_MIN = 800;
    private static final int SMALL_MAX = 1200;
    private static final int MEDIUM_MIN = 1800;
    private static final int MEDIUM_MAX = 2500;
    private static final int LARGE_MIN = 7000;
    private static final int LARGE_MAX = 10000;
    private static final int XLARGE_MIN = 30000;
    private static final int XLARGE_MAX = 45000;

    // Proportions for each job type
    private static final double TINY_RATIO = 0.1;
    private static final double SMALL_RATIO = 0.3;
    private static final double MEDIUM_RATIO = 0.3;
    private static final double LARGE_RATIO = 0.2;
    private static final double XLARGE_RATIO = 0.1;
    private static final int TOTAL_TASKS = 1000;

    // Output file path
    private static final String OUTPUT_FILE = String.format("modules/cloudsim-examples/src/main/java/scheduler/dataset/Synthetic/Synthetic_Dataset_%d.txt", TOTAL_TASKS);

    public static void main(String[] args) {
        List<Integer> workload = generateWorkload(TOTAL_TASKS);

        // Shuffle the task list for random distribution
        Collections.shuffle(workload);

        // Save to file
        try {
            saveToFile(workload, OUTPUT_FILE);
            System.out.println("Workload saved to " + OUTPUT_FILE);
        } catch (IOException e) {
            System.err.println("Error saving workload to file: " + e.getMessage());
        }
    }

    public static List<Integer> generateWorkload(int totalTasks) {
        List<Integer> tasks = new ArrayList<>();
        Random random = new Random(CloudletConfig.SEED);

        int tinyTasks = (int) (totalTasks * TINY_RATIO);
        int smallTasks = (int) (totalTasks * SMALL_RATIO);
        int mediumTasks = (int) (totalTasks * MEDIUM_RATIO);
        int largeTasks = (int) (totalTasks * LARGE_RATIO);
        int xlargeTasks = (int) (totalTasks * XLARGE_RATIO);

        generateTasks(tasks, tinyTasks, TINY_MIN, TINY_MAX, random);
        generateTasks(tasks, smallTasks, SMALL_MIN, SMALL_MAX, random);
        generateTasks(tasks, mediumTasks, MEDIUM_MIN, MEDIUM_MAX, random);
        generateTasks(tasks, largeTasks, LARGE_MIN, LARGE_MAX, random);
        generateTasks(tasks, xlargeTasks, XLARGE_MIN, XLARGE_MAX, random);

        return tasks;
    }

    private static void generateTasks(List<Integer> tasks, int count, int min, int max, Random random) {
        for (int i = 0; i < count; i++) {
            int taskSize = random.nextInt(max - min + 1) + min;
            tasks.add(taskSize);
        }
    }

    private static void saveToFile(List<Integer> tasks, String filePath) throws IOException {
        try (FileWriter writer = new FileWriter(filePath)) {
            for (int taskSize : tasks) {
                writer.write(taskSize + "\n");
            }
        }
    }
}

