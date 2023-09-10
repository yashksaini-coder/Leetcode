# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        # Create a dictionary to map original nodes to their corresponding new nodes
        node_map = {}
        
        # First pass: create new nodes and populate the dictionary
        current = head
        while current:
            node_map[current] = Node(current.val)
            current = current.next
        
        # Second pass: update the next and random pointers of the new nodes
        current = head
        while current:
            if current.next:
                node_map[current].next = node_map[current.next]
            if current.random:
                node_map[current].random = node_map[current.random]
            current = current.next
        
        # Return the head of the new list
        return node_map[head]
