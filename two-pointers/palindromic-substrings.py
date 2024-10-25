class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = 0

        # Create a 2D array to store whether a substring is a palindrome
        dp = [[False] * n for _ in range(n)]

        # All single characters are palindromic
        for i in range(n):
            dp[i][i] = True
            count += 1

        # Check palindromes for substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1

        # Check palindromes for substrings of length 3 or more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1

        return count
