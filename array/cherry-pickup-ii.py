class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])

        # Initialize a 3D DP array
        dp = [[[-1] * cols for _ in range(cols)] for _ in range(rows)]

        def helper(row, col1, col2):
            # Base case: reached the bottom row
            if row == rows:
                return 0

            # Check if the result is already calculated
            if dp[row][col1][col2] != -1:
                return dp[row][col1][col2]

            # Collect cherries for both robots
            cherries = grid[row][col1] + (col1 != col2) * grid[row][col2]

            # Check all possible moves for both robots
            max_cherries = 0
            for next_col1 in range(col1 - 1, col1 + 2):
                for next_col2 in range(col2 - 1, col2 + 2):
                    if 0 <= next_col1 < cols and 0 <= next_col2 < cols:
                        max_cherries = max(max_cherries, helper(row + 1, next_col1, next_col2))

            # Update the DP array
            dp[row][col1][col2] = cherries + max_cherries
            return dp[row][col1][col2]

        return helper(0, 0, cols - 1)
