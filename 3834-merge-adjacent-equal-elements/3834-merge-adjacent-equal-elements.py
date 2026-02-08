class Solution(object):
    def mergeAdjacent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L=[]
        for i in nums:
            L.append(i)
            while (len(L)>=2 and L[-2]==L[-1]):
                a=L.pop(); L.pop(); L.append(a*2)
        return L  