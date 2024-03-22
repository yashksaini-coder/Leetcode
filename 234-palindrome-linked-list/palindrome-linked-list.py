# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        slow = head
        fast = head
        prev = None

        # Find the middle of the linked list and reverse the first half
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        if fast:
            slow = slow.next

        while prev and slow:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next

        return True