class Solution {

    public int longestPalindrome(String s) {
        Map<Character, Integer> frequencyMap = new HashMap<>();
        for (char c : s.toCharArray()) {
            frequencyMap.put(c, frequencyMap.getOrDefault(c, 0) + 1);
        }

        int res = 0;
        boolean hasOddFrequency = false;
        for (int freq : frequencyMap.values()) {
            if ((freq % 2) == 0) {
                res += freq;
            } else {
                res += freq - 1;
                hasOddFrequency = true;
            }
        }
        if (hasOddFrequency) return res + 1;

        return res;
    }
}