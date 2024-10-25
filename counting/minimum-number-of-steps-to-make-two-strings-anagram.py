class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # Count the occurrences of each character in both strings
        count_s = [0] * 26
        count_t = [0] * 26

        for char in s:
            count_s[ord(char) - ord('a')] += 1

        for char in t:
            count_t[ord(char) - ord('a')] += 1

        # Calculate the difference in counts between the two strings
        diff = 0
        for i in range(26):
            diff += abs(count_s[i] - count_t[i])

        # The minimum steps required is half of the differences
        return diff // 2

# Example usage:
solution = Solution()
print(solution.minSteps("bab", "aba"))  # Output: 1
print(solution.minSteps("leetcode", "practice"))  # Output: 5
print(solution.minSteps("anagram", "mangaar"))  # Output: 0
