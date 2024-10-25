class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        
        # Initialize the result with the first row
        result = [[1]]
        
        # Generate the subsequent rows
        for i in range(1, numRows):
            prev_row = result[-1]
            new_row = [1]  # The first element is always 1
            
            for j in range(1, i):
                new_element = prev_row[j - 1] + prev_row[j]
                new_row.append(new_element)
            
            new_row.append(1)  # The last element is always 1
            result.append(new_row)
        
        return result

# Example usage:
numRows = 5
solution = Solution()
print(solution.generate(numRows))
