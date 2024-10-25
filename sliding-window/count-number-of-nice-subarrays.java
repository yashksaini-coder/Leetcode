class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        int n=nums.length;
        int ans=0, t=0;
        int cnt[] = new int[n+1];
        cnt[0]=1;
        for(int v : nums){
            t += v&1;
            if(t-k>=0){
                ans += cnt[t-k];
            }
            cnt[t]++;
        }
        return ans;
    }
}