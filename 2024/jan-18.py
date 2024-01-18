class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Initialize an array to store the number of ways for each step
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1
        dp[1] = 1
        
        # Calculate the number of ways for each step
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

# Example usage:
solution = Solution()
print(solution.climbStairs(2))  # Output: 2
print(solution.climbStairs(3))  # Output: 3
