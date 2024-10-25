class Solution {

    public TreeNode bstToGst(TreeNode root) {
        // Store the inorder traversal in an array.
        List<Integer> inorderTraversal = new ArrayList<>();
        inorder(root, inorderTraversal);

        // Reverse the array to get descending order.
        Collections.reverse(inorderTraversal);

        // Modify the values in the tree.
        replaceValues(root, inorderTraversal);
        return root;
    }

    // Perform any traversal of your choice to store node values.
    private void inorder(TreeNode root, List<Integer> inorderTraversal) {
        if (root == null) {
            return;
        }
        inorder(root.left, inorderTraversal);
        inorderTraversal.add(root.val);
        inorder(root.right, inorderTraversal);
    }

    // Function to modify the values in the tree.
    private void replaceValues(TreeNode root, List<Integer> inorderTraversal) {
        if (root == null) {
            return;
        }
        replaceValues(root.left, inorderTraversal);
        replaceValues(root.right, inorderTraversal);

        int nodeSum = 0;
        // Replace node with values greater than the current value.
        for (int i : inorderTraversal) {
            if (i > root.val) {
                nodeSum += i;
            } else {
                break;
            }
        }

        root.val += nodeSum;
    }
}