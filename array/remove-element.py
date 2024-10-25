class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # Initialize the pointer for the new length of the modified array
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Replace the element to be removed with the new element
                k += 1
        
        return k  # k represents the new length of the modified array

# Example usage
solution = Solution()

