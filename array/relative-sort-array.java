class Solution {

    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        List<Integer> result = new ArrayList<>();

        // Traverse through the relative order array
        for (int i = 0; i < arr2.length; i++) {
            // Traverse through the target array
            for (int j = 0; j < arr1.length; j++) {
                // If element in target array matches with relative order element
                if (arr1[j] == arr2[i]) {
                    // Add it to the result array
                    result.add(arr1[j]);
                    // Mark the element in target array as visited
                    arr1[j] = -1;
                }
            }
        }

        // Sort the remaining elements in the target array
        Arrays.sort(arr1);
        // Add the remaining elements to the result array
        for (int i = 0; i < arr1.length; i++) {
            if (arr1[i] != -1) {
                result.add(arr1[i]);
            }
        }

        // Convert ArrayList to array
        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}