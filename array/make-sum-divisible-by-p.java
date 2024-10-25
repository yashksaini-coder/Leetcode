class Solution {
    public int minSubarray(int[] nums, int p) {
    int sum = 0;    
    for(int x : nums)
    sum = (sum + x)%p;
  
    int mod = sum%p; 
    if(mod==0)
    return 0;

    int ans = nums.length;
    HashMap<Integer, Integer>hm = new HashMap<>();
    hm.put(0, -1);
    int currSumMod = 0;
    for(int i=0; i<nums.length; i++)
    {
      currSumMod = (currSumMod+nums[i])%p;
      int neededMod = (currSumMod - mod + p)%p;
      if(hm.containsKey(neededMod))
      ans = Math.min(ans, i-hm.get(neededMod));
      hm.put(currSumMod, i);
    }
     return ans==nums.length ? -1 : ans;
    }
}