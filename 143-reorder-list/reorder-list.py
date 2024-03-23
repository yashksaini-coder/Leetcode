class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # Step 1: Split the list into two halves using slow and fast pointers
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split point is at slow.next
        second_half = slow.next
        slow.next = None  # Break the link between first and second halves
        
        # Step 2: Reverse the second half of the list
        prev = None
        current = second_half
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        second_half = prev
        
        # Step 3: Merge the two halves by alternating nodes
        first_half = head
        while first_half and second_half:
            first_half_next = first_half.next
            second_half_next = second_half.next
            
            # Update pointers to merge nodes
            first_half.next = second_half
            second_half.next = first_half_next
            
            # Move to the next pair of nodes
            first_half = first_half_next
            second_half = second_half_next
