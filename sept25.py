class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Initialize dictionaries to store character frequencies
        s_count = {}
        t_count = {}
        
        # Count character frequencies in string s
        for char in s:
            s_count[char] = s_count.get(char, 0) + 1
        
        # Count character frequencies in string t
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        
        # Find the character with different counts in t compared to s
        for char in t_count:
            if char not in s_count or t_count[char] > s_count[char]:
                return char

# Test cases
solution = Solution()
print(solution.findTheDifference("abcd", "abcde"))  # Output: "e"
print(solution.findTheDifference("", "y"))  # Output: "y"
