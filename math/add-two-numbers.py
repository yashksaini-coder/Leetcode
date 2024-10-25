# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(0)  # Create a dummy head for the result linked list
        current = dummy_head     # Initialize the current node to the dummy head
        carry = 0                # Initialize the carry to 0

        while l1 or l2 or carry:
            # Get the values of the current nodes or 0 if they are None
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            # Calculate the sum of the current digits and the carry
            total = x + y + carry
            carry = total // 10  # Update the carry
            
            # Create a new node with the ones digit of the total
            current.next = ListNode(total % 10)
            
            # Move to the next nodes if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
            # Move to the next node in the result linked list
            current = current.next
        
        return dummy_head.next  # Return the result linked list starting from the next node of the dummy head
