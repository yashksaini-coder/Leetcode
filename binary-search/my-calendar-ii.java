class MyCalendarTwo {
    private List<int[]> bookings, overlaps;
    public MyCalendarTwo() {
        bookings = new ArrayList<>();
        overlaps = new ArrayList<>();
    }
    public boolean book(int start, int end) {
        for (int[] i : overlaps) {
            if (start < i[1] && end > i[0]) return false;
        }
        for (int[] j : bookings) {
            if (start < j[1] && end > j[0]) {
                overlaps.add(new int[]{Math.max(start, j[0]), Math.min(end, j[1])});
            }
        }
        bookings.add(new int[]{start, end});
        return true;
    }
}