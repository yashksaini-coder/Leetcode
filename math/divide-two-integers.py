class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Handle overflow cases
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle special cases
        if divisor == 0:
            return INT_MAX if dividend > 0 else INT_MIN
        if dividend == 0:
            return 0
        
        # Determine the sign of the result
        negative_result = (dividend < 0) ^ (divisor < 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            temp_divisor = divisor
            multiple = 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            dividend -= temp_divisor
            quotient += multiple
        
        if negative_result:
            quotient = -quotient
        
        # Handle overflow cases
        if quotient > INT_MAX:
            return INT_MAX
        elif quotient < INT_MIN:
            return INT_MIN
        
        return quotient
