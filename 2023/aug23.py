class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        import heapq
        
        # Count the frequency of each character
        char_count = Counter(s)
        
        # Create a max heap to store characters by their frequency
        max_heap = []
        for char, count in char_count.items():
            heapq.heappush(max_heap, (-count, char))
        
        # Initialize variables to track the previous character and its count
        prev_char = None
        prev_count = 0
        
        # Initialize the result string
        result = []
        
        # Construct the result string by interleaving characters
        while max_heap:
            count, char = heapq.heappop(max_heap)
            
            # Add the previous character back to the heap if its count is still positive
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            
            # Append the current character to the result
            result.append(char)
            
            # Update the previous character and its count
            prev_char = char
            prev_count = count + 1  # Since we're using negative counts in the heap
            
        # If the result string has the same length as the original string, return the result
        if len(result) == len(s):
            return ''.join(result)
        else:
            return ""
