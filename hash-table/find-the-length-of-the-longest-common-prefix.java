import java.util.HashMap;

class Solution {
    public int longestCommonPrefix(int[] arr1, int[] arr2) {
        HashMap<String, Integer> prefixMap = new HashMap<>();
        
        // Step 1: Build the prefix map for arr1
        for (int num : arr1) {
            String strNum = Integer.toString(num);
            String prefix = "";
            for (char ch : strNum.toCharArray()) {
                prefix += ch;
                prefixMap.put(prefix, prefixMap.getOrDefault(prefix, 0) + 1);
            }
        }
        
        int maxLength = 0;
        
        // Step 2: Check for common prefixes in arr2
        for (int num : arr2) {
            String strNum = Integer.toString(num);
            String prefix = "";
            for (char ch : strNum.toCharArray()) {
                prefix += ch;
                if (prefixMap.containsKey(prefix)) {
                    maxLength = Math.max(maxLength, prefix.length());
                }
            }
        }
        
        return maxLength;
    }
}