# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pseudoPalindromicPaths(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def isPseudoPalindrome(path_freq):
            odd_count = 0
            for freq in path_freq.values():
                if freq % 2 != 0:
                    odd_count += 1
                if odd_count > 1:
                    return False
            return True

        def dfs(node, path_freq):
            if not node:
                return 0

            path_freq[node.val] += 1

            if not node.left and not node.right:
                # Leaf node, check if the path is pseudo-palindromic
                count = 1 if isPseudoPalindrome(path_freq) else 0
            else:
                # Non-leaf node, continue DFS
                count = dfs(node.left, path_freq.copy()) + dfs(node.right, path_freq.copy())

            path_freq[node.val] -= 1  # Backtrack

            return count

        return dfs(root, defaultdict(int))
