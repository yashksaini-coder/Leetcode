class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplicates = []
        
        for num in nums:
            index = abs(num)
            if nums[index - 1] < 0:
                duplicates.append(index)
            else:
                
                nums[index - 1] *= -1
        
        return duplicates
