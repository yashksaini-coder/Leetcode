class Solution:
    def combinationSum(self, candidates, target):
        def backtrack(start, target, current_combination):
            if target == 0:
                result.append(current_combination[:])
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                current_combination.append(candidates[i])
                backtrack(i, target - candidates[i], current_combination)
                current_combination.pop()

        result = []
        backtrack(0, target, [])
        return result

# Example test cases
candidates1 = [2, 3, 6, 7]
target1 = 7

candidates2 = [2, 3, 5]
target2 = 8

candidates3 = [2]
target3 = 1

solution = Solution()

