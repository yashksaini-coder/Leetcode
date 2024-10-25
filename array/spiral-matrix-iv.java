/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[][] spiralMatrix(int rows, int columns, ListNode head) {
        int[][] matrix = new int[rows][];
        for (int i = 0; i < rows; i++) {
            matrix[i] = new int [columns];
            Arrays.fill(matrix[i], -1);
        }

        int topRow = 0, bottomRow = rows - 1, leftColumn = 0, rightColumn = columns - 1;
        while (head != null) {
        
            for (int col = leftColumn; col <= rightColumn && head != null; col++) {
                matrix[topRow][col] = head.val;
                head = head.next;
            }
            topRow++;

        
            for (int row = topRow; row <= bottomRow && head != null; row++) {
                matrix[row][rightColumn] = head.val;
                head = head.next;
            }
            rightColumn--;

 
            for (int col = rightColumn; col >= leftColumn && head != null; col--) {
                matrix[bottomRow][col] = head.val;
                head = head.next;
            }
            bottomRow--;

       
            for (int row = bottomRow; row >= topRow && head != null; row--) {
                matrix[row][leftColumn] = head.val;
                head = head.next;
            }
            leftColumn++;
        }

        return matrix;
    }
}