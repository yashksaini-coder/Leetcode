class Solution {

    public int appendCharacters(String s, String t) {
        int first = 0, longestPrefix = 0;

        while (first < s.length() && longestPrefix < t.length()) {
            if (s.charAt(first) == t.charAt(longestPrefix)) {
                longestPrefix++;
            }
            first++;
        }

        return t.length() - longestPrefix;
    }
}