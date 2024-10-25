class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        def isUnique(combination):
            return len(set(combination)) == len(combination)

        def backtrack(index, current, max_length):
            if isUnique(current):
                max_length[0] = max(max_length[0], len(current))

            for i in range(index, len(arr)):
                backtrack(i + 1, current + arr[i], max_length)

        max_length = [0]
        backtrack(0, "", max_length)
        return max_length[0]

# Example usage:
solution = Solution()
print(solution.maxLength(["un", "iq", "ue"]))  # Output: 4
print(solution.maxLength(["cha", "r", "act", "ers"]))  # Output: 6
print(solution.maxLength(["abcdefghijklmnopqrstuvwxyz"]))  # Output: 26
