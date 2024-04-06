class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        indices_to_remove = set()

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if not stack:
                    indices_to_remove.add(i)
                else:
                    stack.pop()

        indices_to_remove.update(stack)

        result = []
        for i, char in enumerate(s):
            if i not in indices_to_remove:
                result.append(char)

        return ''.join(result)
