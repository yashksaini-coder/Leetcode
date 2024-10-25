class Solution {
public:
    int minDifference(vector<int>& nums) {
        int numsSize = nums.size();

        // If the array has 4 or fewer elements, return 0
        if (numsSize <= 4) return 0;

        sort(nums.begin(), nums.end());

        int minDiff = INT_MAX;

        // Four scenarios to compute the minimum difference
        for (int left = 0, right = numsSize - 4; left < 4; left++, right++) {
            minDiff = min(minDiff, nums[right] - nums[left]);
        }

        return minDiff;
    }
};