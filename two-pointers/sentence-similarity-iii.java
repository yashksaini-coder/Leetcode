class Solution {
    private String[] splitWords(String sentence) {
        return sentence.split(" ");
    }

    public boolean areSentencesSimilar(String sentence1, String sentence2) {
        String[] words1 = splitWords(sentence1);
        String[] words2 = splitWords(sentence2);
        if (words1.length < words2.length) {
            String[] temp = words1;
            words1 = words2;
            words2 = temp;
        }

        int start = 0, end = 0;
        int n1 = words1.length, n2 = words2.length;
        while (start < n2 && words1[start].equals(words2[start])) {
            start++;
        }
        while (end < n2 && words1[n1 - end - 1].equals(words2[n2 - end - 1])) {
            end++;
        }
        return start + end >= n2;
    }
}