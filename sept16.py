class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def bfs(threshold):
            visited = set()
            queue = [(0, 0)]
            
            while queue:
                x, y = queue.pop(0)
                visited.add((x, y))
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and abs(heights[nx][ny] - heights[x][y]) <= threshold:
                        queue.append((nx, ny))
            
            return (rows - 1, cols - 1) in visited
        
        left, right = 0, 10**6
        
        while left < right:
            mid = (left + right) // 2
            
            if bfs(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

# Test cases
solution = Solution()

# Test case 1
heights1 = [[1,2,2],[3,8,2],[5,3,5]]
print(solution.minimumEffortPath(heights1))  # Output: 2

# Test case 2
heights2 = [[1,2,3],[3,8,4],[5,3,5]]
print(solution.minimumEffortPath(heights2))  # Output: 1

# Test case 3
heights3 = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
print(solution.minimumEffortPath(heights3))  # Output: 0
