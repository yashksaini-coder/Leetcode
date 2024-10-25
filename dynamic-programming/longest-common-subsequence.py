class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m, n = len(text1), len(text2)

        # Initialize a 2D array to store the lengths of common subsequences
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the dp array using dynamic programming
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The result is stored in the bottom-right cell of the dp array
        return dp[m][n]

# Example usage:
solution = Solution()
text1 = "abcde"
text2 = "ace"
result = solution.longestCommonSubsequence(text1, text2)
print(result)  # Output: 3
