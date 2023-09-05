from collections import deque

class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # Push the new element onto queue1
        self.queue1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        # Move all elements from queue1 to queue2 except the last one
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        # The last element in queue1 is the one to be removed (top of the stack)
        top_element = self.queue1.popleft()

        # Swap the names of queue1 and queue2 to make queue2 empty
        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_element

    def top(self):
        """
        :rtype: int
        """
        # This is similar to the pop operation, but we don't remove the element
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        # The last element in queue1 is the top of the stack
        top_element = self.queue1[0]

        # Move the element to queue2 for consistency
        self.queue2.append(self.queue1.popleft())

        # Swap the names of queue1 and queue2 to make queue2 empty
        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_element

    def empty(self):
        """
        :rtype: bool
        """
        # Queue1 will be empty if and only if the stack is empty
        return not bool(self.queue1)

# Example usage:
myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())   # Output: 2
print(myStack.pop())   # Output: 2
print(myStack.empty()) # Output: False
