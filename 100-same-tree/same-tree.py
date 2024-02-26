# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # Base case: Both nodes are None (empty tree)
        if not p and not q:
            return True

        # Check if either p or q is None (one tree is empty while the other is not)
        if not p or not q:
            return False

        # Check if the values of the current nodes are equal
        if p.val != q.val:
            return False

        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
