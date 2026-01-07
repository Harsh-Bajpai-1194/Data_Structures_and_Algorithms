class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        L=[]
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    L.append(prices[i]-prices[j])
                    break
            else:
                L.append(prices[i])
        return L+[prices[-1]]