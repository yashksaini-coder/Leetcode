class Solution {

    public String reverseParentheses(String s) {
        Stack<Integer> openParenthesesIndices = new Stack<>();
        StringBuilder result = new StringBuilder();

        for (char currentChar : s.toCharArray()) {
            if (currentChar == '(') {
                // Store the current length as the start index for future reversal
                openParenthesesIndices.push(result.length());
            } else if (currentChar == ')') {
                int start = openParenthesesIndices.pop();
                // Reverse the substring between the matching parentheses
                reverse(result, start, result.length() - 1);
            } else {
                // Append non-parenthesis characters to the processed string
                result.append(currentChar);
            }
        }

        return result.toString();
    }

    private void reverse(StringBuilder sb, int start, int end) {
        while (start < end) {
            char temp = sb.charAt(start);
            sb.setCharAt(start++, sb.charAt(end));
            sb.setCharAt(end--, temp);
        }
    }
}