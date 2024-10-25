from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Create a defaultdict to store anagrams
        anagrams = defaultdict(list)
        
        # Iterate through each word in the input list
        for word in strs:
            # Sort the characters in the word to get a unique key
            sorted_word = ''.join(sorted(word))
            # Append the word to the list corresponding to its sorted key
            anagrams[sorted_word].append(word)
        
        # Convert the values of the defaultdict to a list to get the final result
        result = list(anagrams.values())
        
        return result
