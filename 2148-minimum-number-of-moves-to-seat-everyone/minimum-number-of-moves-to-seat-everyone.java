class Solution {

    public int minMovesToSeat(int[] seats, int[] students) {
        Arrays.sort(seats);
        Arrays.sort(students);
        int moves = 0;
        for (int i = 0; i < seats.length; i++) {
            // Add the absolute value of the difference
            // between the position of the seat and the student
            moves += Math.abs(seats[i] - students[i]);
        }
        return moves;
    }
}