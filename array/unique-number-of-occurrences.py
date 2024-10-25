from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Count occurrences of each value using Counter
        occurrences = Counter(arr)

        # Check if the number of occurrences is unique
        unique_counts = set(occurrences.values())
        
        return len(unique_counts) == len(occurrences)

