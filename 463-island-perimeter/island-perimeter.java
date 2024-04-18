class Solution {
    public int islandPerimeter(int[][] grid) {
        int perimeter = 0;
        
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    perimeter += 4; // Add 4 sides for each land cell
                    
                    // Check adjacent cells and subtract if they are also land
                    if (i > 0 && grid[i - 1][j] == 1) {
                        perimeter -= 2; // Subtract 2 sides if adjacent cell is land
                    }
                    if (j > 0 && grid[i][j - 1] == 1) {
                        perimeter -= 2; // Subtract 2 sides if adjacent cell is land
                    }
                }
            }
        }
        
        return perimeter;
    }
}
