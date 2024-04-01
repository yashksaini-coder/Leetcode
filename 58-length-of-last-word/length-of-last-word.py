class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove trailing spaces from the string
        s = s.rstrip()
        # Split the string into words using spaces as delimiter
        words = s.split()
        # Check if there are any words in the string
        if len(words) == 0:
            return 0
        # Return the length of the last word
        return len(words[-1])
