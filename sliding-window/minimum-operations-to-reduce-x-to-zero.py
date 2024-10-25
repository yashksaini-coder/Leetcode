class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        target_sum = sum(nums) - x
        if target_sum < 0:
            return -1
        
        left = 0
        curr_sum = 0
        max_length = -1
        
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            while curr_sum > target_sum:
                curr_sum -= nums[left]
                left += 1
            
            if curr_sum == target_sum:
                max_length = max(max_length, right - left + 1)
        
        if max_length == -1:
            return -1
        
        return len(nums) - max_length

# Test cases
solution = Solution()
nums1 = [1, 1, 4, 2, 3]
x1 = 5
result1 = solution.minOperations(nums1, x1)
print("Minimum operations for nums1:", result1)  # Output should be 2

nums2 = [5, 6, 7, 8, 9]
x2 = 4
result2 = solution.minOperations(nums2, x2)
print("Minimum operations for nums2:", result2)  # Output should be -1

nums3 = [3, 2, 20, 1, 1, 3]
x3 = 10
result3 = solution.minOperations(nums3, x3)
print("Minimum operations for nums3:", result3)  # Output should be 5
