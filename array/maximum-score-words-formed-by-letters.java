class Solution {
    public int maxScoreWords(String[] words, char[] letters, int[] score) {
        // Count the frequency of each letter in the given letters array
        int[] letterCount = new int[26];
        for (char c : letters) {
            letterCount[c - 'a']++;
        }
        
        // Start the backtracking process to find the maximum score
        return backtrack(words, letterCount, score, 0);
    }
    
    private int backtrack(String[] words, int[] letterCount, int[] score, int index) {
        if (index == words.length) {
            return 0;
        }
        
        // Skip the current word
        int skip = backtrack(words, letterCount, score, index + 1);
        
        // Try to include the current word
        String word = words[index];
        int wordScore = 0;
        boolean canForm = true;
        for (char c : word.toCharArray()) {
            letterCount[c - 'a']--;
            if (letterCount[c - 'a'] < 0) {
                canForm = false;
            }
            wordScore += score[c - 'a'];
        }
        
        int include = 0;
        if (canForm) {
            include = wordScore + backtrack(words, letterCount, score, index + 1);
        }
        
        // Backtrack: restore the letter counts
        for (char c : word.toCharArray()) {
            letterCount[c - 'a']++;
        }
        
        // Return the maximum score obtained by either including or skipping the current word
        return Math.max(skip, include);
    }
}
