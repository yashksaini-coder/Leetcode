class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list of empty strings for each row
        rows = [''] * numRows
        
        # Initialize variables for current row and direction
        current_row = 0
        direction = 1  # 1 for down, -1 for up
        
        # Traverse the string character by character
        for char in s:
            rows[current_row] += char
            
            # If we reach the top or bottom row, change direction
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1
            
            current_row += direction
        
        # Concatenate the rows to get the final result
        result = ''.join(rows)
        
        return result
