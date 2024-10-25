class Solution {
    public long maximumImportance(int n, int[][] roads) {
        int[] br = new int[n];
        for(int[] r : roads){
            br[r[0]]++;
            br[r[1]]++;
        }
        int[] cnt = new int[n];
        for(int b : br){
            cnt[b]++;
        }
        long sum = 0;
        long val = 1;
        for(long i = 0; i < n; i++){
            for(int j = 0; j < cnt[(int)i]; j++){
                sum += i*val++;
            }
        }
        return sum;
    }
}