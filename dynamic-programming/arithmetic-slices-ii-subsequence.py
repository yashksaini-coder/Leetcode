class Solution:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        total_count = 0  # Total count of arithmetic subsequences

        # dp is a list of dictionaries to store the counts for each index
        dp = [{} for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]

                # If the difference is not in the dp[j], default to 0
                count_j = dp[j].get(diff, 0)

                # Update the count for the current index
                dp[i][diff] = dp[i].get(diff, 0) + count_j + 1

                # Add the count to the total_count
                total_count += count_j

        return total_count

# Example usage:
solution = Solution()
nums1 = [2, 4, 6, 8, 10]
print(solution.numberOfArithmeticSlices(nums1))  # Output: 7

nums2 = [7, 7, 7, 7, 7]
print(solution.numberOfArithmeticSlices(nums2))  # Output: 16
