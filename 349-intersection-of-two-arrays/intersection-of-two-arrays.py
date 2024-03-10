class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Convert arrays to sets
        set1, set2 = set(nums1), set(nums2)
        
        # Find the intersection of sets
        result_set = set1.intersection(set2)
        
        # Convert the result set back to a list
        result = list(result_set)
        
        return result
