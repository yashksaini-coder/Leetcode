class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        increasing = decreasing = True
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False
            elif nums[i] < nums[i - 1]:
                increasing = False
        
        return increasing or decreasing

# Test cases
solution = Solution()
print(solution.isMonotonic([1, 2, 2, 3]))  # Output: True
print(solution.isMonotonic([6, 5, 4, 4]))  # Output: True
print(solution.isMonotonic([1, 3, 2]))  # Output: False
