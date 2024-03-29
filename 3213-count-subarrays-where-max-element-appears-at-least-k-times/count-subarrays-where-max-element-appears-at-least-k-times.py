class Solution(object):
    def countSubarrays(self, nums, k):
        count = 0
        left = 0
        max_freq = 0
        max_element = max(nums)
        for right in range(len(nums)):
            if nums[right] == max_element:
                max_freq += 1
            while max_freq >= k:
                count += len(nums) - right
                if nums[left] == max_element:
                    max_freq -= 1
                left += 1
        return count
