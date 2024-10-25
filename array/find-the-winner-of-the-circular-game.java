class Solution {

    public int findTheWinner(int n, int k) {
        // Initialize list of N friends, labeled from 1-N
        List<Integer> circle = new LinkedList<Integer>();
        for (int i = 1; i <= n; i++) {
            circle.add(i);
        }

        // Maintain the index of the friend to start the count on
        int startIndex = 0;

        // Perform eliminations while there is more than 1 friend left
        while (circle.size() > 1) {
            // Calculate the index of the friend to be removed
            int removalIndex = (startIndex + k - 1) % circle.size();

            // Erase the friend at removalIndex
            circle.remove(removalIndex);

            // Update startIndex for the next round
            startIndex = removalIndex;
        }

        return circle.getFirst();
    }
}