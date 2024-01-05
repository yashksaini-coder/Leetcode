class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

# Example usage:
solution = Solution()
nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
print(solution.lengthOfLIS(nums1))  # Output: 4

nums2 = [0, 1, 0, 3, 2, 3]
print(solution.lengthOfLIS(nums2))  # Output: 4

nums3 = [7, 7, 7, 7, 7, 7, 7]
print(solution.lengthOfLIS(nums3))  # Output: 1
