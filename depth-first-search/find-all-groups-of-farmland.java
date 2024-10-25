class Solution {
    public int[][] findFarmland(int[][] land) {
        List<int[]> farmlandGroups = new ArrayList<>();
        int rows = land.length;
        int cols = land[0].length;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (land[i][j] == 1) {
                    int[] group = dfs(land, i, j);
                    farmlandGroups.add(group);
                }
            }
        }

        int[][] result = new int[farmlandGroups.size()][4];
        for (int i = 0; i < farmlandGroups.size(); i++) {
            result[i] = farmlandGroups.get(i);
        }

        return result;
    }

    private int[] dfs(int[][] land, int row, int col) {
        int rows = land.length;
        int cols = land[0].length;

        int[] group = { row, col, row, col }; // Initialize group coordinates

        // Expand group horizontally
        while (col + 1 < cols && land[row][col + 1] == 1) {
            land[row][col] = 0; // Mark as visited
            col++;
        }
        group[3] = col;

        // Expand group vertically
        while (row + 1 < rows && land[row + 1][col] == 1) {
            land[row][col] = 0; // Mark as visited
            row++;
        }
        group[2] = row;

        // Mark the entire group as visited
        for (int i = group[0]; i <= group[2]; i++) {
            for (int j = group[1]; j <= group[3]; j++) {
                land[i][j] = 0;
            }
        }

        return group;
    }
}
