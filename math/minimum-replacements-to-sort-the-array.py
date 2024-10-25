class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        ops = 0

        prev = nums[n - 1]

        for i in range(n - 2, -1, -1):
            if nums[i] > prev:
                k = math.ceil(nums[i] / prev)
                ops += k - 1
                prev = nums[i] // k
            else:
                prev = nums[i]
        return ops