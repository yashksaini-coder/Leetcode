class Solution {

    public int numWaterBottles(int numBottles, int numExchange) {
        int consumedBottles = 0;

        while (numBottles >= numExchange) {
            // Consume numExchange full bottles.
            consumedBottles += numExchange;
            numBottles -= numExchange;

            // Exchange them for one full bottle.
            numBottles++;
        }

        // Consume the remaining numBottles (<numExchange).
        return consumedBottles + numBottles;
    }
}