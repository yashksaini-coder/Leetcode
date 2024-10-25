import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public String[] findRelativeRanks(int[] score) {
        HashMap<Integer, String> rankMap = new HashMap<>();
        String[] medals = {"Gold Medal", "Silver Medal", "Bronze Medal"};
        int n = score.length;
        
        int[] sortedScores = Arrays.copyOf(score, n);
        Arrays.sort(sortedScores);
        for (int i = 0; i < n; i++) {
            if (i < 3) {
                rankMap.put(sortedScores[n - i - 1], medals[i]);
            } else {
                rankMap.put(sortedScores[n - i - 1], String.valueOf(i + 1));
            }
        }
        String[] result = new String[n];
        for (int i = 0; i < n; i++) {
            result[i] = rankMap.get(score[i]);
        }        
        return result;
    }
}
