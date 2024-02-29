from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        queue = deque([root])
        level = 0

        while queue:
            level_size = len(queue)
            prev_val = float('-inf') if level % 2 == 0 else float('inf')

            for i in range(level_size):
                node = queue.popleft()

                # Check the conditions for Even-Odd tree
                if (level % 2 == 0 and (node.val % 2 == 0 or node.val <= prev_val)) or \
                   (level % 2 == 1 and (node.val % 2 == 1 or node.val >= prev_val)):
                    return False

                prev_val = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return True
