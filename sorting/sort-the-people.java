class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        int n = names.length;
        Map<Integer, String> mapping = new HashMap<>();
        // Step 1 Map
        for (int i = 0; i < n; ++i) {
            mapping.put(heights[i], names[i]);
        }
        // Step 2 Sort
        Arrays.sort(heights);
        for (int i = 0; i < n / 2; ++i) {
            int temp = heights[i];
            heights[i] = heights[n - 1 - i];
            heights[n - 1 - i] = temp;
        }
        // Step 3 Fill the new array 
        for (int i = 0; i < n; ++i) {
            names[i] = mapping.get(heights[i]);
        }

        return names;
    }
}