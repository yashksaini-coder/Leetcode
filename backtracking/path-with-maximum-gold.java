class Solution {
    public int getMaximumGold(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int maxGold = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != 0) {
                    maxGold = Math.max(maxGold, dfs(grid, i, j));
                }
            }
        }
        
        return maxGold;
    }
    
    private int dfs(int[][] grid, int i, int j) {
        int m = grid.length;
        int n = grid[0].length;
        
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == 0) {
            return 0;
        }
        
        int currentGold = grid[i][j];
        grid[i][j] = 0; 
        int maxGold = 0;
        maxGold = Math.max(maxGold, dfs(grid, i + 1, j)); // Move down
        maxGold = Math.max(maxGold, dfs(grid, i - 1, j)); // Move up
        maxGold = Math.max(maxGold, dfs(grid, i, j + 1)); // Move right
        maxGold = Math.max(maxGold, dfs(grid, i, j - 1)); // Move left
        
        grid[i][j] = currentGold; // Backtrack
        
        return maxGold + currentGold;
    }
}
