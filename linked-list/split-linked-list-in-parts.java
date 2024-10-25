class Solution {
    public ListNode[] splitListToParts(ListNode head, int k) {
        int n = 0;
        ListNode curr = head;
        while (curr != null) {
            n++;  
            curr = curr.next;
        }
        
        int base = n / k;  
        int extra = n % k;  
        
        ListNode[] res = new ListNode[k];
        curr = head;
        for (int i = 0; i < k; i++) {
            ListNode part_head = curr;  
            int part_size = base + (extra > 0 ? 1 : 0);
            extra--;  
            for (int j = 0; j < part_size - 1 && curr != null; j++) {
                curr = curr.next;
            }
            if (curr != null) {
                ListNode next_part = curr.next;
                curr.next = null;  
                curr = next_part;  
            }
            
            res[i] = part_head;  
        }
        
        return res;
    }
}