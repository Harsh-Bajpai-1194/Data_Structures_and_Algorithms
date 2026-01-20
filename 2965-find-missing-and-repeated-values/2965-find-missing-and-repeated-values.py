class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        L=[]
        for i in grid: L+=i
        L.sort()
        L1=[]
        for i in L:
            if L.count(i)==2: L1.append(i)
        L1=list(set(L1))
        L=list(set(L))
        L.sort()
        L.insert(0,0)
        for i in range(len(L)):
            if i!=L[i]:
                L1.append(i)
                return L1
        return L1+[L[-1]+1]