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
    public boolean evaluateTree(TreeNode root) {
        if (root == null) return false; // base case for null root
        if (root.val == 0) return false; // leaf node with value 0
        if (root.val == 1) return true;  // leaf node with value 1
        
        boolean leftValue = evaluateTree(root.left);
        boolean rightValue = evaluateTree(root.right);
        
        if (root.val == 2) return leftValue || rightValue; // OR operation
        if (root.val == 3) return leftValue && rightValue; // AND operation
        
        return false; // default return for invalid node values
    }
}
