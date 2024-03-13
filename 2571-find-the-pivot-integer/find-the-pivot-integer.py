class Solution(object):
    def pivotInteger(self, n):
        sum_val = (n * (n + 1)) // 2
        sumx = 0

        for i in range(1, n + 1):
            sumx += i

            if 2 * sumx == sum_val + i:
                return i

        return -1


solution = Solution()
n = 8
result = solution.pivotInteger(n)
print(result)  # Output: 6
