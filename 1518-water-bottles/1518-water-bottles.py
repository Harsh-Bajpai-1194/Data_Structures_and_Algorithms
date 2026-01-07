class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        n,e=numBottles,numExchange
        return n+(n-1)//(e-1)