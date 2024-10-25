class Solution {
    public TreeNode addOneRow(TreeNode root, int val, int depth) {
        if (depth == 1) {
            TreeNode newNode = new TreeNode(val);
            newNode.left = root;
            return newNode;
        }
        addOneRowHelper(root, val, depth, 1);
        return root;
    }
    
    private void addOneRowHelper(TreeNode node, int val, int depth, int currentDepth) {
        if (node == null) {
            return;
        }
        
        if (currentDepth == depth - 1) {
            TreeNode leftChild = new TreeNode(val);
            leftChild.left = node.left;
            node.left = leftChild;
            
            TreeNode rightChild = new TreeNode(val);
            rightChild.right = node.right;
            node.right = rightChild;
            
            return;
        }
        
        addOneRowHelper(node.left, val, depth, currentDepth + 1);
        addOneRowHelper(node.right, val, depth, currentDepth + 1);
    }
}
