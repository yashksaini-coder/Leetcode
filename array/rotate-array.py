class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Ensure k is within the range of array size
        
        # Reverse the entire array
        self.reverse(nums, 0, n - 1)
        
        # Reverse the first k elements
        self.reverse(nums, 0, k - 1)
        
        # Reverse the remaining elements
        self.reverse(nums, k, n - 1)
    
    def reverse(self, nums: list[int], start: int, end: int) -> None:
        """
        Helper function to reverse elements in nums from 'start' to 'end'.
        """
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

