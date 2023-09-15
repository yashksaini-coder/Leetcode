class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Helper function to calculate the Manhattan distance between two points
        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        # Helper function to find the parent of a node in a disjoint-set data structure
        def find_parent(node, parent):
            if parent[node] == node:
                return node
            parent[node] = find_parent(parent[node], parent)
            return parent[node]
        
        # Initialize a list to store the parent of each point
        n = len(points)
        parent = list(range(n))
        
        # Create a list to store edges and their corresponding distances
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                distance = manhattan_distance(points[i], points[j])
                edges.append((distance, i, j))
        
        # Sort the edges by distance in ascending order
        edges.sort()
        
        # Initialize variables to keep track of the MST and its cost
        mst_edges = 0
        mst_cost = 0
        
        # Iterate through the sorted edges and add them to the MST if they don't form a cycle
        for edge in edges:
            distance, u, v = edge
            parent_u = find_parent(u, parent)
            parent_v = find_parent(v, parent)
            
            if parent_u != parent_v:
                parent[parent_u] = parent_v
                mst_cost += distance
                mst_edges += 1
                
                # Early exit if all points are connected
                if mst_edges == n - 1:
                    break
        
        return mst_cost


import matplotlib.pyplot as plt

# Input points
points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]

# Extract x and y coordinates of the points
x = [point[0] for point in points]
y = [point[1] for point in points]

# Create a scatter plot for the points
plt.scatter(x, y, label='Points', color='blue')

# Annotate the points with their coordinates
for i, point in enumerate(points):
    plt.annotate(f'({point[0]}, {point[1]})', (x[i], y[i]), textcoords="offset points", xytext=(0, 10), ha='center')

# Set axis labels and chart title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of Points')

# Show the chart
plt.grid()
plt.legend()
plt.show()
