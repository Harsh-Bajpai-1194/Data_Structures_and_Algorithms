class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans=numBottles
        while numBottles>=numExchange:
            numBottles=numBottles-numExchange
            numExchange,ans,numBottles=numExchange+1,ans+1,numBottles+1
        return ans