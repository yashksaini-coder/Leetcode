class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix_product = [1] * n
        suffix_product = [1] * n
        
        # Calculate prefix products
        for i in range(1, n):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
        
        # Calculate suffix products
        for i in range(n - 2, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i + 1]
        
        # Calculate final result
        result = [prefix_product[i] * suffix_product[i] for i in range(n)]
        
        return result

solution = Solution()
nums = [1, 2, 3, 4]
result = solution.productExceptSelf(nums)
print(result)  # Output: [24, 12, 8, 6]
