class Solution:
    def findMatrix(self, v):
        um = {}
        for i in v:
            um[i] = um.get(i, 0) + 1

        ans = []
        while um:
            temp = []
            to_erase = []
            for f, s in um.items():
                temp.append(f)
                s -= 1
                if s == 0:
                    to_erase.append(f)
                um[f] = s
            ans.append(temp)
            for i in to_erase:
                del um[i]
        return ans

# Example usage:
solution = Solution()
print(solution.findMatrix([1, 3, 4, 1, 2, 3, 1]))  # Output: [[1, 3, 4, 2], [1, 3], [1]]
print(solution.findMatrix([1, 2, 3, 4]))           # Output: [[1, 2, 3, 4]]
