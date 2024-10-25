
//Unordered Map
class Solution {
    public int[] frequencySort(int[] nums) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        
        // Count the frequency of each number
        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }
        
        // Convert the array to Integer list for sorting
        Integer[] numsArray = Arrays.stream(nums).boxed().toArray(Integer[]::new);
        
        // Sort based on frequency and value
        Arrays.sort(numsArray, (a, b) -> {
            if (!freqMap.get(a).equals(freqMap.get(b))) {
                return freqMap.get(a) - freqMap.get(b); // Sort by frequency
            } else {
                return b - a; // Sort by value in decreasing order
            }
        });
        
        // Convert back to int array
        return Arrays.stream(numsArray).mapToInt(Integer::intValue).toArray();
    }
}