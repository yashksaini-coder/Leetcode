class Solution(object):
    def longestValidParentheses(self,s):
        stack = []  # Use a stack to keep track of the indices of '('
        max_length = 0  # Initialize the maximum length to 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  # Push the index of '(' to the stack
            else:
                if stack and s[stack[-1]] == '(':  # If stack is not empty and the top element is '('
                    stack.pop()  # Pop the top '('
                    if not stack:
                        # If the stack is empty, calculate the length from the beginning of the string
                        max_length = max(max_length, i + 1)
                    else:
                        # Calculate the length from the last unmatched '(' in the stack
                        max_length = max(max_length, i - stack[-1])
                else:
                    stack.append(i)  # Push the index of ')' to the stack to mark it as invalid
        
        return max_length
