class Solution {
    public long wonderfulSubstrings(String word) {
        int n = word.length();
        long[] count = new long[1024]; // 2^10, representing all possible bitmasks for the 10 lowercase letters

        int bitmask = 0;
        count[bitmask] = 1; // Initialize with an empty string

        long result = 0;

        for (int i = 0; i < n; i++) {
            bitmask ^= 1 << (word.charAt(i) - 'a'); // Toggle the bit for the current letter

            // Count substrings with each possible bitmask by adding the counts of substrings with previously seen bitmasks
            result += count[bitmask];

            // Count substrings where exactly one letter has odd frequency by adding counts of substrings with all possible toggled bitmasks
            for (int j = 0; j < 10; j++) {
                result += count[bitmask ^ (1 << j)];
            }

            // Update the count for the current bitmask
            count[bitmask]++;
        }

        return result;
    }
}
