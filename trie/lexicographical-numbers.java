class Solution {
    public List<Integer> lexicalOrder(int n) {
        List<Integer> result = new ArrayList<>();
        int current = 1;
        
        for (int i = 0; i < n; i++) {
            result.add(current);
            
            if (current * 10 <= n) {
                current *= 10;  // Move to the next level by multiplying by 10
            } else {
                while (current % 10 == 9 || current + 1 > n) {
                    current /= 10;  // Backtrack if we are at the end of a level
                }
                current++;  // Move to the next number
            }
        }
        
        return result;
    }
}
