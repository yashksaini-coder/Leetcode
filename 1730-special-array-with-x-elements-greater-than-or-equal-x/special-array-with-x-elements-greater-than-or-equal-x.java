class Solution {
    private int getFirstGreaterOrEqual(int[] nums, int val) {
        int start = 0;
        int end = nums.length - 1;

        int index = nums.length;
        while (start <= end) {
            int mid = (start + end) / 2;

            if (nums[mid] >= val) {
                index = mid;
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        return index;
    }

    public int specialArray(int[] nums) {
        Arrays.sort(nums);

        int N = nums.length;
        for (int i = 1; i <= N; i++) {
            int k = getFirstGreaterOrEqual(nums, i);

            if (N - k == i) {
                return i;
            }
        }

        return -1;
    }
}