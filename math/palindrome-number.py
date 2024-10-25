class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Convert the integer to a string
        x_str = str(x)
        
        # Check if the string is equal to its reverse
        return x_str == x_str[::-1]

