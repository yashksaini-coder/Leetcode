class Solution {
    public int[] sortArray(int[] nums) {
        int[] arr = new int[100001];
        int max = Integer.MIN_VALUE, min = Integer.MAX_VALUE;
        int x = 0;
        for (int i : nums) {
            x = 50000 + i;
            arr[x]++;
            if (min > x)
                min = x;
            if (max < x)
                max = x;
        }
        int k = nums.length - 1, n = k + 1;
        for (int i = max; i >= min; i--) {
            if (arr[i] == 0)
                continue;
            int len = arr[i];
            while (len-- > 0)
                nums[k--] = i - 50000;
        }
        return nums;
    }
}