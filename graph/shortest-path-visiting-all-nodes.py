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

