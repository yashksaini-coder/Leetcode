class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Initialize the current level with the poured amount in the top glass
        current_level = [poured]
        
        # Traverse each row up to the target row
        for row in range(query_row):
            # Initialize the next level with the appropriate number of glasses for the current row
            next_level = [0.0] * (row + 2)
            
            # Traverse each glass in the current level
            for glass in range(len(current_level)):
                # Calculate overflow and distribute it to the adjacent glasses in the next level
                overflow = (current_level[glass] - 1.0) / 2.0
                if overflow > 0.0:
                    next_level[glass] += overflow
                    next_level[glass + 1] += overflow
            
            # Update the current level with the next level for the next iteration
            current_level = next_level
        
        # Return the drink level in the target glass (clamped to 1.0 if overflowed)
        return min(1.0, current_level[query_glass])

  solution = Solution()

# Test Case 1
# Pour 1 cup of champagne into the top glass.
# Expected output: 0.0 since the champagne doesn't overflow to the next row.
print(solution.champagneTower(1, 1, 1))

# Test Case 2
# Pour 2 cups of champagne into the top glass. It overflows equally to the glasses below.
# Expected output: 0.5 in the target glass (row 1, glass 1).
print(solution.champagneTower(2, 1, 1))

# Test Case 3
# Pour 100000009 cups of champagne into the top glass. It overflows to various glasses below.
# Expected output: 1.0 in the target glass (row 33, glass 17).
print(solution.champagneTower(100000009, 33, 17))

# Test Case 4
# Pour 0 cups of champagne. All glasses remain empty.
# Expected output: 0.0 in any target glass.
print(solution.champagneTower(0, 33, 17))

# Test Case 5
# Pour 10 cups of champagne into the top glass. It overflows to the glasses below.
# Expected output: 1.0 in the target glass (row 3, glass 2).
print(solution.champagneTower(10, 3, 2))
