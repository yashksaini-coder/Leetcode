class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n = len(arr)
        dp = [0] * n

        for i in range(n):
            current_max = 0
            for j in range(1, min(k, i + 1) + 1):
                current_max = max(current_max, arr[i - j + 1])
                dp[i] = max(dp[i], (dp[i - j] if i - j >= 0 else 0) + current_max * j)

        return dp[-1]
