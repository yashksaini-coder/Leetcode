class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        int start = 0;
        int currentCost = 0;
        int maxLength = 0;

        for (int end = 0; end < s.length(); end++) {
            currentCost += Math.abs(s.charAt(end) - t.charAt(end));

            while (currentCost > maxCost) {
                currentCost -= Math.abs(s.charAt(start) - t.charAt(start));
                start++;
            }

            maxLength = Math.max(maxLength, end - start + 1);
        }

        return maxLength;
    }
}
