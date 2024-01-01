class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Initialize pointers for both strings
        s_pointer, t_pointer = 0, 0
        
        # Iterate through both strings
        while s_pointer < len(s) and t_pointer < len(t):
            # If characters match, move the s_pointer
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            # Always move the t_pointer
            t_pointer += 1
        
        # If s_pointer reached the end of s, it means s is a subsequence of t
        return s_pointer == len(s)

# Test cases
solution = Solution()
print(solution.isSubsequence("abc", "ahbgdc"))  # Output: True
print(solution.isSubsequence("axc", "ahbgdc"))  # Output: False
