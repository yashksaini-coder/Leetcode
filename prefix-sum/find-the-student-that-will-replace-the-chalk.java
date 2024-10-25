class Solution {
    public int chalkReplacer(int[] chalk, int k) {
        long accSum = 0;
        for (int c : chalk) accSum += c;

        k %= accSum;

        for (int i = 0; i < chalk.length; i++) {
            if (chalk[i] > k) return i;
            k -= chalk[i];
        }
        return -1; 
    }
}