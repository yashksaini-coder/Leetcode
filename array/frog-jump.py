class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)

        dp = {stone:set() for stone in stones}
        dp[0].add(0)


        for i in range(n):
            for k in dp[stones[i]]:
                for step in range(k-1, k+2):
                    if step and stones[i] + step in dp:
                        dp[stones[i] + step].add(step)
        
        return len(dp[stones[-1]]) > 0