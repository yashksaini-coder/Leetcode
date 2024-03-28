class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """       
        n, left, result = len(nums), 0, 0
        freq = defaultdict(int)

        for right in range(n):
            freq[nums[right]] += 1  
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1 
                left += 1
            result = max(result, right - left + 1)
        return result