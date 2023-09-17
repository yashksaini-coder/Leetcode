from collections import deque

class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        if n == 1:
            return 0
        
        # Initialize a set to keep track of visited nodes and their states
        visited = set()
        
        # Initialize the queue with (node, state, cost) where state is a bitmask
        queue = deque([(i, 1 << i, 0) for i in range(n)])
        
        # Initialize the target state where all nodes are visited
        target_state = (1 << n) - 1
        
        # Perform BFS
        while queue:
            node, state, cost = queue.popleft()
            
            if state == target_state:
                return cost
            
            # Explore neighbors
            for neighbor in graph[node]:
                new_state = state | (1 << neighbor)
                if (neighbor, new_state) not in visited:
                    visited.add((neighbor, new_state))
                    queue.append((neighbor, new_state, cost + 1))
        
        return -1  # Return -1 if no path is found

# Example usage:
graph1 = [[1,2,3],[0],[0],[0]]
graph2 = [[1],[0,2,4],[1,3,4],[2],[1,2]]

solution = Solution()
print(solution.shortestPathLength(graph1))  # Output: 4
print(solution.shortestPathLength(graph2))  # Output: 4
