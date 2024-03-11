class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        # Define a custom sorting key
        key = lambda x: order.index(x) if x in order else float('inf')
        
        # Sort the characters in string s based on the custom key
        sorted_s = ''.join(sorted(s, key=key))
        
        return sorted_s
