# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root):
        def dfs(node, min_val, max_val):
            if not node:
                return max_val - min_val

            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)

            left_diff = dfs(node.left, min_val, max_val)
            right_diff = dfs(node.right, min_val, max_val)

            return max(left_diff, right_diff)

        return dfs(root, root.val, root.val)

# Example usage:
# Construct the binary tree from Example 1
root1 = TreeNode(8)
root1.left = TreeNode(3)
root1.right = TreeNode(10)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(6)
root1.right.right = TreeNode(14)
root1.left.right.left = TreeNode(4)
root1.left.right.right = TreeNode(7)
root1.right.right.left = TreeNode(13)

solution = Solution()
print(solution.maxAncestorDiff(root1))  # Output: 7

# Construct the binary tree from Example 2
root2 = TreeNode(1)
root2.right = TreeNode(2)
root2.right.right = TreeNode(3)
root2.right.right.left = TreeNode(0)

print(solution.maxAncestorDiff(root2))  # Output: 3
