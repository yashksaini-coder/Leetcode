class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Step 1: Find the first element from the right that is smaller than its right neighbor
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            # Step 2: Find the smallest element to the right of nums[i] that is greater than nums[i]
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the subarray to the right of nums[i]
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# Example usage
solution = Solution()
nums1 = [1, 2, 3]
solution.nextPermutation(nums1)
print(nums1)  # Output: [1, 3, 2]

nums2 = [3, 2, 1]
solution.nextPermutation(nums2)
print(nums2)  # Output: [1, 2, 3]

nums3 = [1, 1, 5]
solution.nextPermutation(nums3)
print(nums3)  # Output: [1, 5, 1]
