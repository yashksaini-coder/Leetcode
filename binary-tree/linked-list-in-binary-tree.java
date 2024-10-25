class Solution {
    boolean a = false;
    public boolean isSubPath(ListNode head, TreeNode root) {
        help(head,root);
        return a;
    }
    public void help(ListNode head,TreeNode root){
        if(head == null){
            a=true;
            return;
        }
        if(root == null){
            return;
        }
        if(head.val==root.val){
            helper(head.next,root.left);
            helper(head.next,root.right);
        }
        help(head,root.left);
        help(head,root.right);
    }
    public void helper(ListNode head,TreeNode root){
        if(head == null){
            a=true;
            return;
        }
        if(root == null){
            return;
        }
        if(head.val==root.val){
            helper(head.next,root.left);
            helper(head.next,root.right);
        }
    }
}