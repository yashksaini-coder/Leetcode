class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(set(nums))
        
        duplicated_number = sum(nums) - actual_sum
        missing_number = expected_sum - actual_sum
        
        return [duplicated_number, missing_number]

# Example usage:
solution = Solution()
print(solution.findErrorNums([1, 2, 2, 4]))  # Output: [2, 3]
print(solution.findErrorNums([1, 1]))  # Output: [1, 2]
