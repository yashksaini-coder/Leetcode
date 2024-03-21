class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Initialize prev and current pointers
        prev = None
        current = head
        
        # Traverse the list and reverse pointers
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Return the new head of the reversed list
        return prev
