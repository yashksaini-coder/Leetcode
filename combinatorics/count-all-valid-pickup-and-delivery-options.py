class Solution(object):
    def countOrders(self, n):
        ans = 1
        MOD = 10 ** 9 + 7
        for n in range(2, n + 1):
            ans *= n*(2*n-1)
            ans %= MOD
        return ans    
    
