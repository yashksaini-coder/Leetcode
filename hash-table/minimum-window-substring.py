from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        # Initialize pointers and counters
        left, right = 0, 0
        required_chars = Counter(t)
        window_chars = {}
        formed = 0
        ans = float('inf'), None, None

        while right < len(s):
            # Expand the window
            window_chars[s[right]] = window_chars.get(s[right], 0) + 1
            if s[right] in required_chars and window_chars[s[right]] == required_chars[s[right]]:
                formed += 1

            # Contract the window
            while formed == len(required_chars):
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right + 1)

                window_chars[s[left]] -= 1
                if s[left] in required_chars and window_chars[s[left]] < required_chars[s[left]]:
                    formed -= 1

                left += 1

            right += 1

        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]]

# Example usage
solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
print(solution.minWindow("a", "a"))  # Output: "a"
print(solution.minWindow("a", "aa"))  # Output: ""
