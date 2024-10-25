class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []  # Create an empty stack to keep track of opening brackets
        
        # Define a dictionary to map closing brackets to their corresponding opening brackets
        bracket_mapping = {')': '(', '}': '{', ']': '['}
        
        # Iterate through each character in the input string
        for char in s:
            # If it's an opening bracket, push it onto the stack
            if char in bracket_mapping.values():
                stack.append(char)
            # If it's a closing bracket
            elif char in bracket_mapping.keys():
                # Check if the stack is empty or the top of the stack doesn't match the current closing bracket
                if not stack or stack.pop() != bracket_mapping[char]:
                    return False  # Not valid
            else:
                return False  # Invalid character
        
        # If the stack is empty, all brackets were valid
        return len(stack) == 0


s = '(){}[]'
solution = Solution()
is_valid = solution.isValid(s)
print(is_valid)  # This will print True for the given input
