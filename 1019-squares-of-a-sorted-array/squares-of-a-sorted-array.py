class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Create a new array to store squares
        squares = [num ** 2 for num in nums]
        
        # Sort the array of squares
        squares.sort()
        return squares