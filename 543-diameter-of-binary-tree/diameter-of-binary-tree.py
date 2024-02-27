# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Helper function to calculate the height of a subtree
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            # Return the height of the subtree
            return 1 + max(left_height, right_height)

        # Helper function to calculate the diameter of a subtree
        def diameter(node):
            if not node:
                return 0
            # Calculate the diameter for the left and right subtrees
            left_diameter = diameter(node.left)
            right_diameter = diameter(node.right)
            # Return the maximum diameter considering both subtrees and passing through the current node
            return max(left_diameter, right_diameter, height(node.left) + height(node.right))

        # Return the calculated diameter for the entire tree
        return diameter(root)
