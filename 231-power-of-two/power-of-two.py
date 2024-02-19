class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Check if n is positive
        if n <= 0:
            return False
        
        # Check if there is only one set bit in the binary representation of n
        return n & (n - 1) == 0
