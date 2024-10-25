class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

        n = len(jobs)
        dp = [0] * n

        for i in range(n):
            # Binary search to find the latest non-overlapping job
            lo, hi = 0, i - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if jobs[mid][1] <= jobs[i][0]:
                    lo = mid + 1
                else:
                    hi = mid - 1

            # Update dp[i] based on the non-overlapping job found
            dp[i] = max(jobs[i][2] + (dp[lo - 1] if lo > 0 else 0), dp[i - 1] if i > 0 else 0)

        return dp[-1]

# Example usage:
solution = Solution()
startTime1 = [1, 2, 3, 3]
endTime1 = [3, 4, 5, 6]
profit1 = [50, 10, 40, 70]
print(solution.jobScheduling(startTime1, endTime1, profit1))  # Output: 120

startTime2 = [1, 2, 3, 4, 6]
endTime2 = [3, 5, 10, 6, 9]
profit2 = [20, 20, 100, 70, 60]
print(solution.jobScheduling(startTime2, endTime2, profit2))  # Output: 150

startTime3 = [1, 1, 1]
endTime3 = [2, 3, 4]
profit3 = [5, 6, 4]
print(solution.jobScheduling(startTime3, endTime3, profit3))  # Output: 6
