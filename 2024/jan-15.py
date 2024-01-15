class Solution:
    def findWinners(self, matches):
        losses = [0] * 100001

        for winner, loser in matches:
            if losses[winner] == 0:
                losses[winner] = -1

            if losses[loser] == -1:
                losses[loser] = 1
            else:
                losses[loser] += 1

        zero_loss = [i for i in range(1, 100001) if losses[i] == -1]
        one_loss = [i for i in range(1, 100001) if losses[i] == 1]

        return [zero_loss, one_loss]
    
# Test cases
solution = Solution()
matches1 = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(solution.findWinners(matches1))
# Output: [[1,2,10],[4,5,7,8]]

matches2 = [[2,3],[1,3],[5,4],[6,4]]
print(solution.findWinners(matches2))
# Output: [[1,2,5,6],[]]