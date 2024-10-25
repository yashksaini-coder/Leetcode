class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        n = len(colors)
        alice_moves = 0
        bob_moves = 0

        # Check Alice's moves
        for i in range(1, n - 1):
            if colors[i - 1:i + 2] == "AAA":
                alice_moves += 1

        # Check Bob's moves
        for i in range(1, n - 1):
            if colors[i - 1:i + 2] == "BBB":
                bob_moves += 1

        # Determine the winner based on the number of moves
        if alice_moves > bob_moves:
            return True
        else:
            return False

# Test cases
solution = Solution()
print(solution.winnerOfGame("AAABABB"))  # Output: True
print(solution.winnerOfGame("AA"))        # Output: False
print(solution.winnerOfGame("ABBBBBBBAAA"))  # Output: False
