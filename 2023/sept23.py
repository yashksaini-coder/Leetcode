class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # Sort the words by length to optimize the dynamic programming approach
        words.sort(key=lambda x: len(x))
        
        # Create a dictionary to store the longest chain length for each word
        word_chain = {}
        
        # Initialize the maximum chain length
        max_chain_length = 1
        
        for word in words:
            # Initialize the chain length for the current word
            word_chain[word] = 1
            
            # Generate all possible predecessors of the current word
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                
                # Check if the predecessor exists in the word_chain dictionary
                if predecessor in word_chain:
                    # Update the chain length for the current word
                    word_chain[word] = max(word_chain[word], word_chain[predecessor] + 1)
            
            # Update the maximum chain length
            max_chain_length = max(max_chain_length, word_chain[word])
        
        return max_chain_length

# Test cases
solution = Solution()
print(solution.longestStrChain(["a","b","ba","bca","bda","bdca"]))  # Output: 4
print(solution.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))  # Output: 5
print(solution.longestStrChain(["abcd","dbqca"]))  # Output: 1
