class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Mark non-positive integers as n + 1
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        # Mark visited indices by making nums[abs(nums[i]) - 1] negative
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        
        # Find the first positive number by checking if nums[i] is positive
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        # If all positive integers in [1, n] are present, return n + 1
        return n + 1
