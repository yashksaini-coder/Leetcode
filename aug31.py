class Solution(object):
    def minTaps(self, n, ranges):
        dp = [float('inf')] * (n + 1)

        dp[0] = 0

        for i, tap_range in enumerate(ranges):
            left = max(0, i - tap_range)
            right = min(n, i + tap_range)

            for j in range(left, right + 1):
                dp[j] = min(dp[j], dp[left] + 1)

        return dp[n] if dp[n] < float('inf') else -1
