class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even_ptr = 0  # Pointer for even numbers
        odd_ptr = len(nums) - 1  # Pointer for odd numbers
        
        while even_ptr < odd_ptr:
            if nums[even_ptr] % 2 == 1 and nums[odd_ptr] % 2 == 0:
                # Swap the elements at even_ptr and odd_ptr
                nums[even_ptr], nums[odd_ptr] = nums[odd_ptr], nums[even_ptr]
            
            if nums[even_ptr] % 2 == 0:
                even_ptr += 1
            
            if nums[odd_ptr] % 2 == 1:
                odd_ptr -= 1
        
        return nums

# Test case
solution = Solution()
print(solution.sortArrayByParity([3, 1, 2, 4]))  # Output: [4, 2, 3, 1]
