class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        int n = nums.length, prefSum = 0;
        Map<Integer, Integer> firstOcc = new HashMap<>();
        firstOcc.put(0, 0);

        for (int i = 0; i < n; i++) {
            prefSum = (prefSum + nums[i]) % k;
            if (firstOcc.containsKey(prefSum)) {
                if (i + 1 - firstOcc.get(prefSum) >= 2) {
                    return true;
                }
            } else {
                firstOcc.put(prefSum, i + 1);
            }
        }

        return false;
    }
}