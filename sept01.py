class Solution(object):
    def countBits(self,n):
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans


sol=Solution()
n=int(input("Enter a number:-"))
res=sol.countBits(n)
print(res)
