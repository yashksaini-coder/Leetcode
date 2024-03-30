from collections import defaultdict

class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMostK(nums, k):
            count = defaultdict(int)
            left = right = 0
            distinct = 0
            subarrays = 0

            while right < len(nums):
                if count[nums[right]] == 0:
                    distinct += 1
                count[nums[right]] += 1

                while distinct > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        distinct -= 1
                    left += 1

                subarrays += right - left + 1
                right += 1

            return subarrays

        return atMostK(nums, k) - atMostK(nums, k - 1)
