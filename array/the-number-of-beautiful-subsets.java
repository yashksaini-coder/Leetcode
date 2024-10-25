class Solution {
    public int beautifulSubsets(int[] nums, int k) {
        return backtrack(nums, k, 0, new ArrayList<>());
    }

    private int backtrack(int[] nums, int k, int start, List<Integer> current) {
        if (start == nums.length) {
            return current.isEmpty() ? 0 : 1;
        }

        int count = 0;
        // Exclude the current element
        count += backtrack(nums, k, start + 1, current);

        // Include the current element
        boolean isBeautiful = true;
        for (int num : current) {
            if (Math.abs(num - nums[start]) == k) {
                isBeautiful = false;
                break;
            }
        }
        if (isBeautiful) {
            current.add(nums[start]);
            count += backtrack(nums, k, start + 1, current);
            current.remove(current.size() - 1);
        }

        return count;
    }
}
