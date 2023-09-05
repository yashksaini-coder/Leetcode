class Solution(object):
    def findLongestChain(self,pairs):
        # Sort the pairs based on the right end in ascending order.
        pairs.sort(key=lambda x: x[1])
        
        n = len(pairs)
        dp = [1] * n  # Initialize the dp array with all 1s.
        
        for i in range(1, n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

