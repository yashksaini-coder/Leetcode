class Solution {
    public int countMaxOrSubsets(int[] nums) {
        int max = 0;
        for (int n : nums) max |= n;
        return dfs(nums, 0, 0, max);
    }
    private int dfs(int[] nums, int i, int or, int max) {
        if (i == nums.length) return or == max ? 1 : 0;
        return dfs(nums, i + 1, or | nums[i], max) + dfs(nums, i + 1, or, max);
    }
}