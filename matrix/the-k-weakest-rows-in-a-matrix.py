class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        # Step 1: Calculate the number of soldiers in each row
        def count_soldiers(row):
            return row.count(1)
        
        # Step 2: Create a list of tuples (row index, number of soldiers)
        rows = [(i, count_soldiers(mat[i])) for i in range(len(mat))]
        
        # Step 3: Sort the list based on the number of soldiers and row index
        rows.sort(key=lambda x: (x[1], x[0]))
        
        # Step 4: Extract the first k row indices
        result = [row[0] for row in rows[:k]]
        
        return result

# Example usage:
mat1 = [[1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]]
k1 = 3
mat2 = [[1,0,0,0],
        [1,1,1,1],
        [1,0,0,0],
        [1,0,0,0]]
k2 = 2

solution = Solution()
print(solution.kWeakestRows(mat1, k1))  # Output: [2, 0, 3]
print(solution.kWeakestRows(mat2, k2))  # Output: [0, 2]
