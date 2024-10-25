class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0  # If the array is empty, there are no duplicates
        
        k = 1  # Initialize the pointer for the new length of the modified array
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]  # Replace the duplicate with the new element
                k += 1
        
        return k  # k represents the new length of the modified array

# Example usage
solution = Solution()

