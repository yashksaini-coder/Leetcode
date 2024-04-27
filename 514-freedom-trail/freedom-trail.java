import java.util.HashMap;
import java.util.Map;

class Solution {
    public int findRotateSteps(String ring, String key) {
        int n = ring.length();
        int m = key.length();
        Map<String, Integer> memo = new HashMap<>();
        return dfs(ring, key, 0, 0, memo) + m; // Adding m for pressing the center button for each character in key
    }

    private int dfs(String ring, String key, int rIdx, int kIdx, Map<String, Integer> memo) {
        if (kIdx == key.length()) {
            return 0; // All characters in key have been spelled
        }

        String memoKey = rIdx + "-" + kIdx;
        if (memo.containsKey(memoKey)) {
            return memo.get(memoKey); // Return memoized result
        }

        char targetChar = key.charAt(kIdx);
        int minSteps = Integer.MAX_VALUE;

        for (int i = 0; i < ring.length(); i++) {
            if (ring.charAt(i) == targetChar) {
                int clockWiseSteps = Math.abs(rIdx - i);
                int anticlockWiseSteps = ring.length() - clockWiseSteps;
                int steps = Math.min(clockWiseSteps, anticlockWiseSteps);
                int subSteps = dfs(ring, key, i, kIdx + 1, memo);
                minSteps = Math.min(minSteps, steps + subSteps);
            }
        }

        memo.put(memoKey, minSteps); // Memoize the result
        return minSteps;
    }
}
