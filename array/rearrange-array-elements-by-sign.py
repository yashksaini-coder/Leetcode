class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Separate positive and negative numbers
        positive_nums = [num for num in nums if num > 0]
        negative_nums = [num for num in nums if num < 0]

        # Merge positive and negative numbers with alternating signs
        rearranged_array = []
        while positive_nums and negative_nums:
            rearranged_array.append(positive_nums.pop(0))
            rearranged_array.append(negative_nums.pop(0))

        # If any positive or negative numbers are left, append them to the result
        rearranged_array.extend(positive_nums)
        rearranged_array.extend(negative_nums)

        return rearranged_array

# Example usage:
solution = Solution()
nums1 = [3, 1, -2, -5, 2, -4]
print(solution.rearrangeArray(nums1))  # Output: [3, -2, 1, -5, 2, -4]

nums2 = [-1, 1]
print(solution.rearrangeArray(nums2))  # Output: [1, -1]
