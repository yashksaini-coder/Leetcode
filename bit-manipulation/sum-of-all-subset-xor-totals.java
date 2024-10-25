class Solution {
    public int subsetXORSum(int[] nums) {
        return helper(nums, 0, 0);
    }
    
    public int helper(int[] nums, int level, int currentXOR) {
        if (level == nums.length) return currentXOR;
        int include = helper(nums, level + 1, currentXOR ^ nums[level]);
        int exclude = helper(nums, level + 1, currentXOR);
        return include + exclude;
    }
}
