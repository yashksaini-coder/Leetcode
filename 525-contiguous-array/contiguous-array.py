class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        running_sum = 0
        sum_indices = {0: -1}  # Initialize with sum 0 and index -1
        
        for i in range(len(nums)):
            if nums[i] == 0:
                running_sum -= 1
            else:
                running_sum += 1
            
            if running_sum in sum_indices:
                max_length = max(max_length, i - sum_indices[running_sum])
            else:
                sum_indices[running_sum] = i
        
        return max_length
