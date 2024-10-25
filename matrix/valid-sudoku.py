class Solution:
    def isValidSudoku(self, board):
        def is_valid_subbox(row, col):
            seen = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if board[i][j] != ".":
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])
            return True

        for i in range(9):
            row_seen = set()
            col_seen = set()
            for j in range(9):
                # Check rows
                if board[i][j] != ".":
                    if board[i][j] in row_seen:
                        return False
                    row_seen.add(board[i][j])

                # Check columns
                if board[j][i] != ".":
                    if board[j][i] in col_seen:
                        return False
                    col_seen.add(board[j][i])

            # Check sub-boxes
            if i % 3 == 0:
                for j in range(0, 9, 3):
                    if not is_valid_subbox(i, j):
                        return False

        return True

# Example boards
board1 = [["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]]

board2 = [["8","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]]

solution = Solution()

