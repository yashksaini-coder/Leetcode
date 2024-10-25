class Solution {
    public int maximumSwap(int num) {
        // Convert the integer to a string for easy manipulation of digits
        String numStr = Integer.toString(num);
        char[] digits = numStr.toCharArray();
        
        // Initialize maxNum to the original number
        int maxNum = num;
        int n = digits.length;
        
        // Nested loop to try all possible swaps of digits
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                // Swap the digits at indices i and j
                swap(digits, i, j);
                
                // Convert the modified char array back to an integer
                int swappedNum = Integer.parseInt(new String(digits));
                
                // Update maxNum if the new number is larger
                if (swappedNum > maxNum) {
                    maxNum = swappedNum;
                }
                
                // Swap the digits back to restore the original string
                swap(digits, i, j);
            }
        }
        
        // Return the maximum number found
        return maxNum;
    }
    
    // Helper method to swap two digits in the char array
    private static void swap(char[] arr, int i, int j) {
        char temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
