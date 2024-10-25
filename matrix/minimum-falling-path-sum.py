class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        
        # Initialize a copy of the matrix to store the minimum falling path sums
        dp = [[0] * n for _ in range(n)]
        
        # Copy the first row of the original matrix to dp
        for i in range(n):
            dp[0][i] = matrix[0][i]
        
        # Calculate the minimum falling path sums for each cell in dp
        for i in range(1, n):
            for j in range(n):
                dp[i][j] = matrix[i][j] + min(
                    dp[i - 1][j - 1] if j - 1 >= 0 else float('inf'),
                    dp[i - 1][j],
                    dp[i - 1][j + 1] if j + 1 < n else float('inf')
                )
        
        # Return the minimum value in the last row of dp
        return min(dp[-1])

# Example usage:
solution = Solution()
print(solution.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))  # Output: 13
print(solution.minFallingPathSum([[-19,57],[-40,-5]]))  # Output: -59
