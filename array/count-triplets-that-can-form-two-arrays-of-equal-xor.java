class Solution {
    public int countTriplets(int[] arr) {
        int n = arr.length;
        int[] prefixXor = new int[n + 1];
        
        for (int i = 0; i < n; i++) {
            prefixXor[i + 1] = prefixXor[i] ^ arr[i];
        }
        
        int count = 0;
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < k; i++) {
                if (prefixXor[i] == prefixXor[k + 1]) {
                    count += (k - i);
                }
            }
        }
        return count;
    }
}
