class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index

            stack.append(i)

        return result

# Example usage:
solution = Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
result = solution.dailyTemperatures(temperatures)
print(result)  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
