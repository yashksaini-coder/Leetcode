class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        ans= 0
        min_position = max_position = l = -1
        
        for i, num in enumerate(nums):
            # If the number is outside the range [minK, maxK], update the most recent left_bound.
            if num < minK or num > maxK:
                l = i
                
            # If the number is minK or maxK, update the most recent position.
            if num == minK:
                min_position = i
            if num == maxK:
                max_position = i
                
            # The number of valid subarrays equals the number of elements between left_bound and 
            # the smaller of the two most recent positions.
            ans += max(0, min(min_position, max_position) - l)
            
        return ans