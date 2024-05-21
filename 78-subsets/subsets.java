class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> op = new ArrayList<>();
        solve(nums, 0, op, res);
        return res;
    }
    public void solve(int nums[], int start, List<Integer> op, List<List<Integer>> res){
        if(nums.length == start){
            res.add(new ArrayList<>(op));
            return;
        }
        solve(nums, start + 1, op, res);
        op.add(nums[start]);
        solve(nums, start + 1, op, res);
        op.remove(op.size() - 1);
    }
}