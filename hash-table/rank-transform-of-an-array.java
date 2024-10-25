import java.util.*;

class Solution {
    public int[] arrayRankTransform(int[] arr) {
        Map<Integer, Integer> valueToRank = new HashMap<>();
        int[] sortedUniqueNumbers = Arrays.stream(arr).distinct().sorted().toArray();
        
        // Assign ranks to sorted unique elements
        for (int i = 0; i < sortedUniqueNumbers.length; i++) {
            valueToRank.put(sortedUniqueNumbers[i], i + 1);
        }

        // Replace each element in the original array with its rank
        for (int i = 0; i < arr.length; i++) {
            arr[i] = valueToRank.get(arr[i]);
        }

        return arr; 
    }
}
