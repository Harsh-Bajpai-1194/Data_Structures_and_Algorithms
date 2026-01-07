class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int n=numBottles,e=numExchange;
        return n+floor((n-1)/(e-1));
    }
};