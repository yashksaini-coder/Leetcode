import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] sumOfDistancesInTree(int n, int[][] edges) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        int[] count = new int[n]; // Count of nodes in subtree rooted at each node
        int[] sum = new int[n]; // Sum of distances in subtree rooted at each node

        dfs(0, -1, graph, count, sum); // Perform depth-first search to calculate counts and sums

        int[] result = new int[n];
        result[0] = sum[0]; // Root node's sum is already calculated

        calculateSums(0, -1, graph, count, sum, result, n); // Calculate sums for each node based on parent's sum

        return result;
    }

    private void dfs(int node, int parent, List<List<Integer>> graph, int[] count, int[] sum) {
        count[node] = 1; // Initialize count to 1 for current node
        for (int neighbor : graph.get(node)) {
            if (neighbor != parent) {
                dfs(neighbor, node, graph, count, sum); // Recursively traverse the tree
                count[node] += count[neighbor]; // Update count for current node
                sum[node] += sum[neighbor] + count[neighbor]; // Update sum for current node
            }
        }
    }

    private void calculateSums(int node, int parent, List<List<Integer>> graph, int[] count, int[] sum, int[] result, int n) {
        for (int neighbor : graph.get(node)) {
            if (neighbor != parent) {
                result[neighbor] = result[node] - count[neighbor] + n - count[neighbor];
                calculateSums(neighbor, node, graph, count, sum, result, n);
            }
        }
    }
}
