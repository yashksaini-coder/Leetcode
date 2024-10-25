class Solution {

    public boolean isNStraightHand(int[] hand, int groupSize) {
        int handSize = hand.length;
        if (handSize % groupSize != 0) {
            return false;
        }

        // TreeMap to store the count of each card value
        Map<Integer, Integer> cardCount = new TreeMap<>();
        for (int i = 0; i < handSize; i++) {
            cardCount.put(hand[i], cardCount.getOrDefault(hand[i], 0) + 1);
        }

        // Process the cards until the map is empty
        while (cardCount.size() > 0) {
            // Get the smallest card value
            int current_card = cardCount.entrySet().iterator().next().getKey();
            // Check each consecutive sequence of groupSize cards
            for (int i = 0; i < groupSize; i++) {
                // If a card is missing or has exhausted its occurrences
                if (!cardCount.containsKey(current_card + i)) return false;
                cardCount.put(
                    current_card + i,
                    cardCount.get(current_card + i) - 1
                );
                // Remove the card value if its occurrences are exhausted
                if (cardCount.get(current_card + i) == 0) cardCount.remove(
                    current_card + i
                );
            }
        }

        return true;
    }
}