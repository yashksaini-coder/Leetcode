# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Create a linked list from the given list 'head'
def createLinkedList(head, pos):
    if not head:
        return None
    nodes = [ListNode(x) for x in head]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        
        # Initialize two pointers: slow and fast
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next         # Move slow by one step
            fast = fast.next.next   # Move fast by two steps
            
            if slow == fast:
                return True  # If they meet, there is a cycle
        
        return False  # If fast reaches the end, there is no cycle


sol = Solution()
print("TEST CASE\n")
print("head = [3,2,0,-4]")
print("pos = 1")
head = [3,2,0,-4]
pos = 1

linked_list = createLinkedList(head, pos)
res=sol.hasCycle(linked_list)
print("Output:-\n",res)

