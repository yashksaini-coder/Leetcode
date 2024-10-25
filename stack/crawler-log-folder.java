class Solution {

    public int minOperations(String[] logs) {
        int folderDepth = 0;

        // Iterate through each log operation
        for (String currentOperation : logs) {
            // Go up one directory if "../" is encountered, but don't go above the root
            if (currentOperation.equals("../")) {
                folderDepth = Math.max(0, folderDepth - 1);
            }
            // Increase depth if the log is not 'stay in the current directory'
            else if (!currentOperation.equals("./")) {
                // Go down one directory
                folderDepth++;
            }
            // Ignore "./" operations as they don't change the current folder
        }

        return folderDepth;
    }
}