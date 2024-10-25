class Solution {
    public static String removeKdigits(String num, int k) {
        if (k == num.length()) {
            return "0";
        }

        char[] digits = num.toCharArray();
        char[] stack = new char[digits.length];
        int stackTop = -1;
        int removalCount = k;

        for (int i = 0; i < digits.length; i++) {
            while (removalCount > 0 && stackTop >= 0 && stack[stackTop] > digits[i]) {
                stackTop--;
                removalCount--;
            }
            stackTop++;
            stack[stackTop] = digits[i];
        }

        int nonZeroStart = 0;

        while (stack[nonZeroStart] == '0' && nonZeroStart < digits.length - k - 1) {
            nonZeroStart++;
        }

        return String.valueOf(stack, nonZeroStart, digits.length - k - nonZeroStart);
    }
}