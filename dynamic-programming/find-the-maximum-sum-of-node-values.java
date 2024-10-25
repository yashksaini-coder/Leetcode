class Solution {
    public long maximumValueSum(int[] nums, int k, int[][] edges) {
        long[][] memo = new long[nums.length][2];
        for (long[] row : memo) {
            Arrays.fill(row, -1);
        }
        return maxSumOfNodes(0, 1, nums, k, memo);
    }

    private long maxSumOfNodes(int index, int isEven, int[] nums, int k,
            long[][] memo) {
        if (index == nums.length) {
            return isEven == 1 ? 0 : Integer.MIN_VALUE;
        }
        if (memo[index][isEven] != -1) {
            return memo[index][isEven];
        }
        long noXorDone = nums[index] + maxSumOfNodes(index + 1, isEven, nums, k, memo);
        long xorDone = (nums[index] ^ k) +
                maxSumOfNodes(index + 1, isEven ^ 1, nums, k, memo);

        // Memoize and return the result
        return memo[index][isEven] = Math.max(xorDone, noXorDone);
    }
}