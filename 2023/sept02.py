class Solution:
    def solve(self, s, mp, dp, index):
        if index >= len(s):
            return 0
        if dp[index] != -1:
            return dp[index]

        currStr = ""
        minExtra = len(s)
        for cutIdx in range(index, len(s)):
            currStr += s[cutIdx]

            # If the string is not in the dictionary, we have to delete it as they are extra characters
            currExtra = 0 if currStr in mp else len(currStr)
            nextExtra = self.solve(s, mp, dp, cutIdx + 1)
            totalExtra = currExtra + nextExtra

            minExtra = min(minExtra, totalExtra)

        dp[index] = minExtra
        return minExtra

    def minExtraChar(self, s, dictionary):
        dp = [-1] * len(s)
        mp = {}
        for word in dictionary:
            mp[word] = 1

        ans = self.solve(s, mp, dp, 0)
        return ans

# Example usage:
s = "leetscode"
dictionary = ["leet", "code", "leetcode"]
solution = Solution()
result = solution.minExtraChar(s, dictionary)
print(result)  # Output: 1
