class Solution {

    public double averageWaitingTime(int[][] customers) {
        int nextIdleTime = 0;
        long netWaitTime = 0;

        for (int i = 0; i < customers.length; i++) {
            // The next idle time for the chef is given by the time of delivery
            // of current customer's order.
            nextIdleTime = Math.max(customers[i][0], nextIdleTime) +
            customers[i][1];

            // The wait time for the current customer is the difference between
            // his delivery time and arrival time.
            netWaitTime += nextIdleTime - customers[i][0];
        }

        // Divide by total customers to get average.
        double averageWaitTime = (double) netWaitTime / customers.length;
        return averageWaitTime;
    }
}