class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(arr)
        stack = []
        result = 0

        # Calculate the contribution of each element to the final result
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                j = stack.pop()
                k = stack[-1] if stack else -1
                result += arr[j] * (i - j) * (j - k)
                result %= MOD
            stack.append(i)

        # Handle the remaining elements in the stack
        while stack:
            j = stack.pop()
            k = stack[-1] if stack else -1
            result += arr[j] * (n - j) * (j - k)
            result %= MOD

        return result

# Example usage:
solution = Solution()
print(solution.sumSubarrayMins([3, 1, 2, 4]))  # Output: 17
print(solution.sumSubarrayMins([11, 81, 94, 43, 3]))  # Output: 444
