import java.util.HashSet;
import java.util.Set;

class Solution {
    public int minExtraChar(String s, String[] dictionary) {
        Set<String> dict = new HashSet<>();
        for (String word : dictionary) {
            dict.add(word);
        }
        int n = s.length();
        int[] dp = new int[n + 1];

        // Initialize dp array
        for (int i = 0; i <= n; i++) {
            dp[i] = n; // Maximum extra characters possible
        }
        dp[0] = 0; // No extra characters needed for an empty string

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                String sub = s.substring(j, i);
                if (dict.contains(sub)) {
                    dp[i] = Math.min(dp[i], dp[j]); // No extra characters if sub is in dictionary
                }
            }
            dp[i] = Math.min(dp[i], dp[i - 1] + 1); // Extra character if we don't use dp[i-1]
        }

        return dp[n];
    }
}
