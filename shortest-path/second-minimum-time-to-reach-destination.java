class Solution {
    public int secondMinimum(int n, int[][] edges, int time, int change) {
        // Create adjacency list for the graph
        Map<Integer, List<Integer>> adj = new HashMap<>();
        for (int[] edge : edges) {
            int a = edge[0], b = edge[1];
            adj.computeIfAbsent(a, value -> new ArrayList<>()).add(b);
            adj.computeIfAbsent(b, value -> new ArrayList<>()).add(a);
        }

        // Initialize distance arrays and frequency array
        int[] dist1 = new int[n + 1];
        int[] dist2 = new int[n + 1];
        int[] freq = new int[n + 1];

        // Initialize arrays
        for (int i = 1; i <= n; i++) {
            dist1[i] = Integer.MAX_VALUE;
            dist2[i] = Integer.MAX_VALUE;
        }

        // Priority queue for Dijkstra's algorithm
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        pq.offer(new int[]{1, 0});
        dist1[1] = 0;

        while (!pq.isEmpty()) {
            int[] temp = pq.poll();
            int node = temp[0];
            int currentTime = temp[1];

            freq[node]++;

            // If the node is being visited for the second time and is node n, return the answer
            if (freq[node] == 2 && node == n) {
                return currentTime;
            }

            // If the current light is red, wait till the path turns green
            if ((currentTime / change) % 2 == 1) {
                currentTime = change * (currentTime / change + 1) + time;
            } else {
                currentTime = currentTime + time;
            }

            if (!adj.containsKey(node)) {
                continue;
            }

            for (int neighbor : adj.get(node)) {
                // Ignore nodes that have already popped out twice
                if (freq[neighbor] == 2) {
                    continue;
                }

                // Update dist1 if it's more than the current time and store its value in dist2
                if (dist1[neighbor] > currentTime) {
                    dist2[neighbor] = dist1[neighbor];
                    dist1[neighbor] = currentTime;
                    pq.offer(new int[]{neighbor, currentTime});
                } else if (dist2[neighbor] > currentTime && dist1[neighbor] != currentTime) {
                    dist2[neighbor] = currentTime;
                    pq.offer(new int[]{neighbor, currentTime});
                }
            }
        }
        return 0; // If the second minimum distance is not found
    }
}