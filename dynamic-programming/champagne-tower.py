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