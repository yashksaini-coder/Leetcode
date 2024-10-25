class Solution {
    public int[] sortJumbled(int[] mapping, int[] nums) {
        Map<Integer, Integer> numberMapping = new HashMap<>();

        for (int num : nums) {
            if (!numberMapping.containsKey(num)) {
                numberMapping.put(num, translateInteger(num, mapping));
            }
        }

        Integer[] numsBoxed = Arrays.stream(nums).boxed().toArray(Integer[]::new);
        Arrays.sort(numsBoxed, (a, b) -> Integer.compare(numberMapping.get(a), numberMapping.get(b)));

        for (int i = 0; i < nums.length; i++) {
            nums[i] = numsBoxed[i];
        }

        return nums;
    }

    private int translateInteger(int num, int[] mapping) {
        char[] digits = Integer.toString(num).toCharArray();
        for (int i = 0; i < digits.length; i++) {
            digits[i] = (char) ('0' + mapping[digits[i] - '0']);
        }
        return Integer.parseInt(new String(digits));
    }
}