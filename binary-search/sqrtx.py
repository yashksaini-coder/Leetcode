class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        left, right = 1, x
        
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        
        # When the loop exits, left will be the largest integer whose square is less than or equal to x.
        # So, we return left - 1 to get the floor square root.
        return left - 1

