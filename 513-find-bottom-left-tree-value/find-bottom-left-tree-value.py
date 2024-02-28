from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None

        # Use a queue for level-order traversal
        queue = deque([root])

        while queue:
            # Pop the current level
            level_size = len(queue)
            leftmost_node = None

            for i in range(level_size):
                node = queue.popleft()

                # Update leftmost_node for the current level
                if i == 0:
                    leftmost_node = node.val

                # Enqueue the child nodes for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # The last leftmost node in the last level will be returned
            result = leftmost_node

        return result
