from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root, start):
        def dfs(node):
            if node is None:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right)

        graph = defaultdict(list)
        dfs(root)
        visited = set()
        queue = deque([start])
        time = -1
        while queue:
            time += 1
            for _ in range(len(queue)):
                current_node = queue.popleft()
                visited.add(current_node)
                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return time

# Example usage:
# Construct the binary tree from Example 1
root1 = TreeNode(1)
root1.left = TreeNode(5)
root1.right = TreeNode(3)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(10)
root1.right.right.left = TreeNode(6)
root1.right.right.right = TreeNode(9)
root1.right.right.right.left = TreeNode(2)

solution = Solution()
print(solution.amountOfTime(root1, 3))  # Output: 4

# Construct a single-node tree from Example 2
root2 = TreeNode(1)
print(solution.amountOfTime(root2, 1))  # Output: 0
