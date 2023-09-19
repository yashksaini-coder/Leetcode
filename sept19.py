class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Phase 1: Find the intersection point of the two pointers
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Phase 2: Find the entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

# Test cases
solution = Solution()
nums1 = [1,3,4,2,2]
result1 = solution.findDuplicate(nums1)
print("Duplicate in nums1:", result1)  # Output should be 2

nums2 = [3,1,3,4,2]
result2 = solution.findDuplicate(nums2)
print("Duplicate in nums2:", result2)  # Output should be 3
