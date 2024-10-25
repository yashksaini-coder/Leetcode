# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Initialize a dummy node before the head
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next and current.next.next:
            # Nodes to be swapped
            first_node = current.next
            second_node = current.next.next
            
            # Swapping
            current.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            
            # Move the pointer to the next pair
            current = first_node
        
        return dummy.next

# Define a separate print_linked_list function
def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next
    print("None")

# Example usage
# Create linked list: 1 -> 2 -> 3 -> 4

# Print the swapped linked list: 2 -> 1 -> 4 -> 3
solution = Solution()
