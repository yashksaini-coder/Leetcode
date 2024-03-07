# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Initialize two pointers: slow and fast
        slow = head
        fast = head
        
        # Iterate until fast reaches the end of the list
        while fast and fast.next:
            # Move slow one step and fast two steps
            slow = slow.next
            fast = fast.next.next
        
        # The slow pointer is now at the middle of the list
        return slow
