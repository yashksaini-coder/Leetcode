class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Initialize pointers for the prefix and suffix
        left, right = 0, len(s) - 1
        
        # Continue as long as the string is not empty and the characters match
        while left < right and s[left] == s[right]:
            # Record the current character
            current_char = s[left]
            
            # Move the left pointer to the right until a different character is found
            while left <= right and s[left] == current_char:
                left += 1
            
            # Move the right pointer to the left until a different character is found
            while left <= right and s[right] == current_char:
                right -= 1
        
        # The remaining string between the pointers is the result
        return right - left + 1
