class Solution {
    private char solve(int term, int k) {
        if (term == 1) {
            return '0'; 
        }

        int len = (1 << term) - 1;
        int mid = len / 2;

        if (mid == k) {
            return '1';
        } else if (k < mid) {
            return solve(term - 1, k);
        } else {
            int new_k = len - k - 1;
            char ans = solve(term - 1, new_k);
            return ans == '1' ? '0' : '1';  
        }
    }

    public char findKthBit(int term, int k) {
        return solve(term, k - 1);
    }
}