class Solution(object):
    def closeStrings(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        freq_s = [0] * 26
        freq_t = [0] * 26

        for ch in s:
            freq_s[ord(ch) - ord('a')] += 1

        for ch in t:
            freq_t[ord(ch) - ord('a')] += 1

        for i in range(26):
            if (freq_s[i] == 0 and freq_t[i] != 0) or (freq_s[i] != 0 and freq_t[i] == 0):
                return False

        freq_s.sort()
        freq_t.sort()

        for i in range(26):
            if freq_s[i] != freq_t[i]:
                return False

        return True

# Example usage:
solution = Solution()
print(solution.closeStrings("abc", "bca"))  # Output: True
print(solution.closeStrings("a", "aa"))  # Output: False
print(solution.closeStrings("cabbba", "abbccc"))  # Output: True
