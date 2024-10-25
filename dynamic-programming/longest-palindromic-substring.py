class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        n = len(s)
        start = 0  # Initialize the start index of the longest palindrome
        max_length = 1  # Initialize the maximum palindrome length

        # Create a table to store whether a substring is a palindrome or not
        is_palindrome = [[False] * n for _ in range(n)]

        # All substrings of length 1 are palindromes
        for i in range(n):
            is_palindrome[i][i] = True

        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                is_palindrome[i][i + 1] = True
                start = i
                max_length = 2

        # Check for palindromes of length greater than 2
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1  # Ending index of the current substring

                if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                    is_palindrome[i][j] = True
                    if length > max_length:
                        start = i
                        max_length = length

        return s[start:start + max_length]
