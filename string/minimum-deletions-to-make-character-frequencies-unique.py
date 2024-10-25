class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Initialize a dictionary to store character frequencies
        char_freq = {}
        
        # Count character frequencies
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        # Initialize a set to track used frequencies
        used_freq = set()
        
        # Initialize the number of deletions
        deletions = 0
        
        # Iterate through character frequencies
        for freq in char_freq.values():
            while freq in used_freq:
                freq -= 1
                deletions += 1
            if freq > 0:
                used_freq.add(freq)
        
        return deletions
