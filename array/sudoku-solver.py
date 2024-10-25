class Solution:
    def solveSudoku(self, board):
        def is_valid(num, row, col):
            # Check if 'num' is valid in the current row, column, and subgrid
            for i in range(9):
                if board[row][i] == num or board[i][col] == num or board[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3] == num:
                    return False
            return True

        def backtrack(row, col):
            if row == 9:
                return True  # We've filled all rows successfully

            if col == 9:
                return backtrack(row + 1, 0)  # Move to the next row

            if board[row][col] != '.':
                return backtrack(row, col + 1)  # Cell is already filled, move to the next

            for num in map(str, range(1, 10)):
                if is_valid(num, row, col):
                    board[row][col] = num
                    if backtrack(row, col + 1):
                        return True
                    board[row][col] = '.'  # If the current path doesn't lead to a solution, backtrack

            return False  # No valid number found, need to backtrack further

        backtrack(0, 0)  # Start solving from the top-left cell
        return board

# Example Sudoku board
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

solution = Solution()
solved_board = solution.solveSudoku(board)
for row in solved_board:
    print(row)
