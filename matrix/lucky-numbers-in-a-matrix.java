class Solution {
    public List<Integer> luckyNumbers (int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        
        int[] row_minimums = new int[rows];
        Arrays.fill(row_minimums, Integer.MAX_VALUE);
        int[] col_maximums = new int[cols];
        
        for (int row_ind = 0; row_ind < rows; ++row_ind) {
            for (int col_ind = 0; col_ind < cols; ++col_ind) {
                int el = matrix[row_ind][col_ind];
                row_minimums[row_ind] = Math.min(row_minimums[row_ind], el);
                col_maximums[col_ind] = Math.max(col_maximums[col_ind], el);
            }
        }
        
        for (int row_ind = 0; row_ind < rows; ++row_ind) {
            for (int col_ind = 0; col_ind < cols; ++col_ind) {
                int el = matrix[row_ind][col_ind];
                if (el == row_minimums[row_ind] && el == col_maximums[col_ind]) {
                    return Collections.singletonList(el);
                }
            }
        }
        
        return Collections.emptyList();
    }
}