class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        L=[]
        for i in order:
            if i not in friends: L.append(i)
        for i in L: order.remove(i)
        return order