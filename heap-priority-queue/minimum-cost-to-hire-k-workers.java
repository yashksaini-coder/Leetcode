import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public double mincostToHireWorkers(int[] quality, int[] wage, int k) {
        int n = quality.length;
        double totalCost = Double.MAX_VALUE;
        int currentTotalQuality = 0;
        
        // Create an array to store the wage-to-quality ratio and quality of each worker
        double[][] wageToQualityRatio = new double[n][2];
        for (int i = 0; i < n; i++) {
            wageToQualityRatio[i][0] = (double) wage[i] / quality[i]; // Calculate ratio
            wageToQualityRatio[i][1] = quality[i]; // Store quality
        }
        
        // Sort workers based on wage-to-quality ratio
        Arrays.sort(wageToQualityRatio, (a, b) -> Double.compare(a[0], b[0]));
        
        // Max heap to store workers with highest qualities
        PriorityQueue<Integer> highestQualityWorkers = new PriorityQueue<>((a, b) -> b - a);
        
        for (double[] worker : wageToQualityRatio) {
            highestQualityWorkers.offer((int) worker[1]); // Push quality to heap
            currentTotalQuality += worker[1]; // Update total quality
            
            if (highestQualityWorkers.size() > k) {
                currentTotalQuality -= highestQualityWorkers.poll(); // Remove highest quality worker
            }
            
            if (highestQualityWorkers.size() == k) {
                double currentCost = currentTotalQuality * worker[0]; // Calculate total cost
                totalCost = Math.min(totalCost, currentCost); // Update minimum cost
            }
        }
        
        return totalCost;
    }
}
