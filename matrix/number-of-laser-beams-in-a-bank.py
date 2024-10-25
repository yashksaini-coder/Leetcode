class Solution(object):
    def numberOfBeams(self, bank):
        prev_row_count = 0
        total = 0

        for row in bank:
            cur_row_count = self.calc(row)
            if cur_row_count == 0:
                continue

            total += cur_row_count * prev_row_count
            prev_row_count = cur_row_count

        return total

    @staticmethod
    def calc(s):
        return s.count('1')

# Example usage:
solution = Solution()
bank1 = ["011001", "000000", "010100", "001000"]
print(solution.numberOfBeams(bank1))  # Output: 8

bank2 = ["000", "111", "000"]
print(solution.numberOfBeams(bank2))  # Output: 0
