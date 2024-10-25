class Solution {

    public List<String> wordBreak(String s, List<String> wordDict) {
        // Convert wordDict to a set for O(1) lookups
        Set<String> wordSet = new HashSet<>(wordDict);
        List<String> results = new ArrayList<>();
        // Start the backtracking process
        backtrack(s, wordSet, new StringBuilder(), results, 0);
        return results;
    }

    private void backtrack(
        String s,
        Set<String> wordSet,
        StringBuilder currentSentence,
        List<String> results,
        int startIndex
    ) {
        // If we've reached the end of the string, add the current sentence to results
        if (startIndex == s.length()) {
            results.add(currentSentence.toString().trim());
            return;
        }

        // Iterate over possible end indices
        for (
            int endIndex = startIndex + 1;
            endIndex <= s.length();
            endIndex++
        ) {
            String word = s.substring(startIndex, endIndex);
            // If the word is in the set, proceed with backtracking
            if (wordSet.contains(word)) {
                int currentLength = currentSentence.length();
                currentSentence.append(word).append(" ");
                // Recursively call backtrack with the new end index
                backtrack(s, wordSet, currentSentence, results, endIndex);
                // Reset currentSentence to its original length
                currentSentence.setLength(currentLength);
            }
        }
    }
}