class Solution:
    def largestPerimeter(self, nums):
        nums.sort()
        _sum = sum(nums)
        n = len(nums)
        for i in range(n - 1, 1, -1):
            _sum -= nums[i]
            if _sum > nums[i]:
                return _sum + nums[i]
        return -1