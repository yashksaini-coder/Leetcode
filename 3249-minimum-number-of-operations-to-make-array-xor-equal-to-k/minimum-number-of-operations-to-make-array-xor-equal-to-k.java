class Solution {
    public int minOperations(int[] nums, int k) {
        int operations = 0;
        int xor = 0;
        for (int num : nums) {
            xor ^= num;
        }
        
        // Check if xor of elements is already k
        if (xor == k) {
            return 0;
        }
        
        // If not, find the xor of elements and k
        int target = xor ^ k;
        
        // Count the number of set bits in the target
        while (target > 0) {
            operations++;
            target &= (target - 1); // clear the rightmost set bit
        }
        
        return operations;
    }
}