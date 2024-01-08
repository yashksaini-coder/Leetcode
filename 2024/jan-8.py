# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root, low, high):
        if not root:
            return 0

        # Initialize the sum
        sum_range = 0

        # If the current node value is in the range, add it to the sum
        if low <= root.val <= high:
            sum_range += root.val

        # Recursively traverse the left and right subtrees
        sum_range += self.rangeSumBST(root.left, low, high)
        sum_range += self.rangeSumBST(root.right, low, high)

        return sum_range

# Example usage:
# Construct the binary tree from the example
root1 = TreeNode(10)
root1.left = TreeNode(5)
root1.right = TreeNode(15)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(7)
root1.right.right = TreeNode(18)

solution = Solution()
print(solution.rangeSumBST(root1, 7, 15))  # Output: 32

# Construct another binary tree from the example
root2 = TreeNode(10)
root2.left = TreeNode(5)
root2.right = TreeNode(15)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(7)
root2.right.left = TreeNode(13)
root2.right.right = TreeNode(18)
root2.left.left.left = TreeNode(1)
root2.left.right.left = TreeNode(6)

print(solution.rangeSumBST(root2, 6, 10))  # Output: 23
