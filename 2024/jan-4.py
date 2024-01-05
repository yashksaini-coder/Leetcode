from collections import Counter

class Solution:
    def minOperations(self, nums):
        mp = Counter(nums)

        count = 0
        for t in mp.values():
            if t == 1:
                return -1
            count += t // 3
            if t % 3:
                count += 1

        return count

# Example usage:
solution = Solution()
nums = [1, 2, 2, 1, 1, 3]
print(solution.minOperations(nums))
