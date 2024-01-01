class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 3:
            return False

        # Initialize the stack to store potential "2" elements
        stack = []
        # Initialize the maximum value seen so far (potential "3")
        max_val = float('-inf')

        # Iterate through the array from right to left
        for i in range(n - 1, -1, -1):
            # If we find a number smaller than max_val, we have a 132 pattern
            if nums[i] < max_val:
                return True

            # While the stack is not empty and the current number is greater
            # than the top of the stack, update max_val and pop elements from the stack
            while stack and nums[i] > stack[-1]:
                max_val = stack.pop()

            # Add the current number to the stack (potential "2")
            stack.append(nums[i])

        return False

# Test cases
solution = Solution()
print(solution.find132pattern([1, 2, 3, 4]))  # Output: False
print(solution.find132pattern([3, 1, 4, 2]))  # Output: True
print(solution.find132pattern([-1, 3, 2, 0]))  # Output: True
