class Solution {
    public int[] xorQueries(int[] arr, int[][] queries) {

        int[] ans = new int[queries.length];
        int[] prefix = new int[arr.length];
        prefix[0] = arr[0];

        // fill the prefix xor array
        for(int i=1; i<arr.length; i++){
            prefix[i] = prefix[i-1] ^ arr[i];
        } 

        for(int i=0; i<queries.length; i++){
            int left = queries[i][0];
            int right = queries[i][1];
            if(left == 0){
                ans[i] = prefix[right];
            }else{
                ans[i] = prefix[right]^prefix[left-1];
            }
        }
        return ans;
    }
}