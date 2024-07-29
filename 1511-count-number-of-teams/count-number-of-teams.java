class Solution {
    public int numTeams(int[] rating) {
        int total = 0;
        int n = rating.length;
        
        for (int i = 0; i < n; i++) {
            int rightLess = 0, rightMore = 0, leftLess = 0, leftMore = 0;

            // Count soldiers after i
            for (int j = i + 1; j < n; j++) {
                if (rating[j] < rating[i]) rightLess++;
                else if (rating[j] > rating[i]) rightMore++;
            }
            
            // Count soldiers before i
            for (int j = 0; j < i; j++) {
                if (rating[j] < rating[i]) leftLess++;
                else if (rating[j] > rating[i]) leftMore++;
            }

            // Calculate the total number of valid teams
            total += rightLess * leftMore + rightMore * leftLess;
        }

        return total;
    }
}