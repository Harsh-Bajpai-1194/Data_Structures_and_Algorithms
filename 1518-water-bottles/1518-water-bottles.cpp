class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int n=numBottles, x=numExchange, drank=0, empty=0;
        while(n>0)
        {
            assert(empty<x);
            n--;
            empty++;
            drank++;
            if (empty==x)
            {
                empty=0;
                n++;
            }
        }
        return drank;
    }
};