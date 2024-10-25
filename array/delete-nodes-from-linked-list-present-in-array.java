class Solution {
    public ListNode modifiedList(int[] nums, ListNode head) {
        int max = 0;
        for(int ele : nums) {
            if(ele > max) max = ele;
        }
        int count[] = new int[max + 1];
        for(int ele : nums) count[ele] = 1;

        ListNode prev = new ListNode(0);
        prev.next = head;
        ListNode result = prev;
        while(head != null) {
            if(head.val <= max && count[head.val] == 1) {
                prev.next = head.next;
                head = head.next;
            }
            else {
                prev = head;
                head = head.next;
            }
        }
        return result.next;
    }
}