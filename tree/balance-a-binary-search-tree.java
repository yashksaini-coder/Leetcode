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

    public TreeNode balanceBST(TreeNode root) {
        // Create a list to store the inorder traversal of the BST
        List<Integer> inorder = new ArrayList<>();
        inorderTraversal(root, inorder);

        // Construct and return the balanced BST
        return createBalancedBST(inorder, 0, inorder.size() - 1);
    }

    private void inorderTraversal(TreeNode root, List<Integer> inorder) {
        // Perform an inorder traversal to store the elements in sorted order
        if (root == null) return;
        inorderTraversal(root.left, inorder);
        inorder.add(root.val);
        inorderTraversal(root.right, inorder);
    }

    private TreeNode createBalancedBST(
        List<Integer> inorder,
        int start,
        int end
    ) {
        // Base case: if the start index is greater than the end index, return null
        if (start > end) return null;

        // Find the middle element of the current range
        int mid = start + (end - start) / 2;

        // Recursively construct the left and right subtrees
        TreeNode leftSubtree = createBalancedBST(inorder, start, mid - 1);
        TreeNode rightSubtree = createBalancedBST(inorder, mid + 1, end);

        // Create a new node with the middle element and attach the subtrees
        TreeNode node = new TreeNode(
            inorder.get(mid),
            leftSubtree,
            rightSubtree
        );
        return node;
    }
}