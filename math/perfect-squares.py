class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Create an array to store the least number of perfect squares that sum to each number
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        # Iterate through each number from 1 to n
        for i in range(1, n + 1):
            # Check all perfect squares less than or equal to i
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[n]
