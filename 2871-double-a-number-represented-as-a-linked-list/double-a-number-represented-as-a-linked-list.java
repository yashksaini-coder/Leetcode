/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode doubleIt(ListNode head) {
        int carry = twice(head);
        if (carry > 0) {
            head = new ListNode(carry, head);
        }
        return head;
    }

    private int twice(ListNode head) {
        if (head == null) {
            return 0;
        }
        int doubledValue = head.val * 2 + twice(head.next);
        head.val = doubledValue % 10;
        return doubledValue / 10;
    }
}