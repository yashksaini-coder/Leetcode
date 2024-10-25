class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Base case: if n is 0, return 1
        if n == 0:
            return 1.0
        
        # Handle negative n
        if n < 0:
            x = 1 / x
            n = -n
        
        # Recursive calculation of x^n
        half_pow = self.myPow(x, n // 2)
        
        # If n is even, x^n = (x^(n/2))^2
        if n % 2 == 0:
            return half_pow * half_pow
        # If n is odd, x^n = x * (x^(n/2))^2
        else:
            return x * half_pow * half_pow

