class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        L,L1=[],{}   
        for i in range(len(groupSizes)):
            j=groupSizes[i]
            if j not in L1:
                L1[j]=[]
            L1[j].append(i)
            if len(L1[j])==j:
                L.append(L1[j])
                L1[j]=[]
        return L