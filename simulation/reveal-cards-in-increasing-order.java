
class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        Arrays.sort(deck);
        Deque<Integer> dq = new LinkedList<>();
        int n = deck.length;
        dq.offerFirst(deck[n - 1]);
        for (int i = n - 2; i >= 0; i--) {
            int x = dq.pollLast();
            dq.offerFirst(x);
            dq.offerFirst(deck[i]);
        }

        int[] ans = new int[n];
        int index = 0;
        while (!dq.isEmpty()) {
            ans[index++] = dq.pollFirst();
        }
        return ans;
    }
}