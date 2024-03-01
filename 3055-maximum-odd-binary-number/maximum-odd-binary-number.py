class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        sorted_chars = []
        ones = []
        result = ""
        
        for char in s:
            sorted_chars.append(char)
      
        for char in sorted_chars:
            if char == "1":
                sorted_chars.remove(char)
                ones.append(char)
                break  
        
        sorted_chars.sort()
        sorted_chars.reverse()
        sorted_chars.extend(ones)  
        
        result = result.join(sorted_chars)  
        
        return result