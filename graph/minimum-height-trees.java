import java.util.*;

class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        List<Integer> result = new ArrayList<>();
        if (n == 1) {
            result.add(0);
            return result;
        }

        Map<Integer, List<Integer>> graph = buildGraph(n, edges);
        Queue<Integer> leaves = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            if (graph.get(i).size() == 1) {
                leaves.offer(i);
            }
        }

        while (n > 2) {
            int size = leaves.size();
            n -= size;

            for (int i = 0; i < size; i++) {
                int leaf = leaves.poll();
                int parent = graph.get(leaf).get(0);
                graph.get(parent).remove(Integer.valueOf(leaf));
                if (graph.get(parent).size() == 1) {
                    leaves.offer(parent);
                }
            }
        }

        result.addAll(leaves);
        return result;
    }

    private Map<Integer, List<Integer>> buildGraph(int n, int[][] edges) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < n; i++) {
            graph.put(i, new ArrayList<>());
        }

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        return graph;
    }
}
