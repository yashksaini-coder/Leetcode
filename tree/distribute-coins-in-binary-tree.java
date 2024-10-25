// Definition for a binary tree node.
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
class Solution {
    private int moves = 0;
    
    public int distributeCoins(TreeNode root) {
        dfs(root);
        return moves;
    }
    
    private int dfs(TreeNode node) {
        if (node == null) return 0;
        
        int leftBalance = dfs(node.left);
        int rightBalance = dfs(node.right);
        
        moves += Math.abs(leftBalance) + Math.abs(rightBalance);
        
        return node.val + leftBalance + rightBalance - 1;
    }
}