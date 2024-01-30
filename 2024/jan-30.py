class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                stack.append(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()

                if token == '+':
                    result = operand1 + operand2
                elif token == '-':
                    result = operand1 - operand2
                elif token == '*':
                    result = operand1 * operand2
                else:  # token == '/'
                    result = int(float(operand1) / operand2)

                stack.append(result)

        return stack.pop()

# Example usage:
solution = Solution()
tokens = ["2", "1", "+", "3", "*"]
result = solution.evalRPN(tokens)
print(result)  # Output: 9
