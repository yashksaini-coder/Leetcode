class Solution(object):
    def reverse(self, x):
        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1

        reversed_x = 0
        while x != 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10

        # Check for overflow
        if reversed_x > 2**31 - 1 or reversed_x < -2**31:
            return 0

        return sign * reversed_x
