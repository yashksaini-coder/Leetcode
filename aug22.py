class Solution(object):
    def convertToTitle(self, columnNumber):
        result = []
        
        while columnNumber > 0:
            columnNumber -= 1  # Adjust to 0-based index
            remainder = columnNumber % 26
            result.append(chr(remainder + ord('A')))
            columnNumber //= 26
        
        result.reverse()  # Reverse the list to get the correct order
        return ''.join(result)

