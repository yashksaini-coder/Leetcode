from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Count the frequency of each character
        char_freq = Counter(s)
        
        # Sort the characters based on their frequency in descending order
        sorted_chars = sorted(char_freq, key=lambda x: char_freq[x], reverse=True)
        
        # Build the sorted string
        result = ''.join(char * char_freq[char] for char in sorted_chars)
        
        return result
