/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public String smallestFromLeaf(TreeNode root) {
        return dfs(root, new StringBuilder()).toString();
    }
    
    private StringBuilder dfs(TreeNode node, StringBuilder current) {
        if (node == null) {
            return null;
        }
        
        current.append((char) ('a' + node.val));  // Append the current node's character
        
        if (node.left == null && node.right == null) {  // If leaf node, return the current string
            return current.reverse();
        }
        
        StringBuilder leftString = dfs(node.left, new StringBuilder(current));  // Traverse left subtree
        StringBuilder rightString = dfs(node.right, new StringBuilder(current));  // Traverse right subtree
        
        if (leftString == null) {  // If left subtree is null, return right subtree's result
            return rightString;
        } else if (rightString == null) {  // If right subtree is null, return left subtree's result
            return leftString;
        } else {  // Compare both subtrees and return the lexicographically smaller one
            return leftString.compareTo(rightString) <= 0 ? leftString : rightString;
        }
    }
}
