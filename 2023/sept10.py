class Solution(object):
    def countOrders(self, n):
        ans = 1
        mod=10**9+7
        for n in range(2, n + 1):
            ans *= n*(2*n-1)
            ans %= mod
        return ans    
    
# Example usage:
solution = Solution()
print(solution.countOrders(1))  # Output: 1
print(solution.countOrders(2))  # Output: 6
print(solution.countOrders(3))  # Output: 90
