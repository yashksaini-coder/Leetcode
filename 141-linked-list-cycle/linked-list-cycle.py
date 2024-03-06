# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Initialize two pointers: slow and fast
        slow = head
        fast = head
        
        # Iterate until fast reaches the end of the list
        while fast and fast.next:
            # Move slow one step and fast two steps
            slow = slow.next
            fast = fast.next.next
            
            # Check if the pointers meet, indicating a cycle
            if slow == fast:
                return True
        
        # If fast reaches the end, there is no cycle
        return False
