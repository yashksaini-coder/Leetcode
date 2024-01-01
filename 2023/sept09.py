class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Initialize a list to store the number of combinations for each target sum
        dp = [0] * (target + 1)
        
        # There's one way to make a sum of 0, which is not choosing any number
        dp[0] = 1
        
        # Iterate through all possible target sums from 1 to the given target
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        
        return dp[target]

nums = [1, 2, 3]
target = 4
solution = Solution()
print(solution.combinationSum4(nums, target))
