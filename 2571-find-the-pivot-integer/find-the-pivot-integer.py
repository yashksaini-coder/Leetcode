class Solution(object):
    def pivotInteger(self, n):
        _sum = n * (n + 1) // 2
        
        root = int(math.sqrt(_sum))
        if root * root == _sum:
            return root
        return -1
solution = Solution()
n = 8
result = solution.pivotInteger(n)
print(result)  # Output: 6
