package scheduler.dataset.Random;

import scheduler.model.CloudletConfig;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 * @Author: Chen
 * @File Name: RandomDatasetGenerator.java
 */

public class RandomDatasetGenerator {
    private static final int TOTAL_TASKS = 1000;

    // Output file path
    private static final String OUTPUT_FILE = String.format("modules/cloudsim-examples/src/main/java/scheduler/dataset/Random/Random_Dataset_%d.txt", TOTAL_TASKS);


    public static void main(String args[]){
        Random rand = new Random(CloudletConfig.SEED);
        List<Long> tasks = new ArrayList<>();

        for (int i = 0; i < CloudletConfig.NUM_CLOUDLETS; i++){
            long length = CloudletConfig.CLOUDLET_LENGTH;
            if (CloudletConfig.RANDOM_LENGTH) {
                long delta = rand.nextInt(CloudletConfig.RANDOM_DELTA * 2) - CloudletConfig.RANDOM_DELTA;
                length = Math.max(CloudletConfig.MIN_LENGTH, length + delta);
            }
            tasks.add(length);
        }

        // Save to file
        try {
            saveToFile(tasks, OUTPUT_FILE);
            System.out.println("Workload saved to " + OUTPUT_FILE);
        } catch (IOException e) {
            System.err.println("Error saving workload to file: " + e.getMessage());
        }
    }



    private static void saveToFile(List<Long> tasks, String filePath) throws IOException {
        try (FileWriter writer = new FileWriter(filePath)) {
            for (long taskSize : tasks) {
                writer.write(taskSize + "\n");
            }
        }
    }
}
