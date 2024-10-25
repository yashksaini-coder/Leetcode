class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Create a 2D array dp to store the number of unique paths
        dp = [[1] * n for _ in range(m)]
        
        # Fill in the dp array using dynamic programming
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        # The value at dp[m-1][n-1] will be the number of unique paths
        return dp[m - 1][n - 1]

