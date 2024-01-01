# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        # Calculate the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Calculate the size of each part and the remainder
        part_size, remainder = divmod(length, k)
        
        # Initialize variables
        result = []
        current = head
        prev = None
        
        # Split the linked list into k parts
        for i in range(k):
            result.append(current)
            for j in range(part_size + (i < remainder) - 1):
                if current:
                    current = current.next
            if current:
                prev, current = current, current.next
                prev.next = None
        
        return result
