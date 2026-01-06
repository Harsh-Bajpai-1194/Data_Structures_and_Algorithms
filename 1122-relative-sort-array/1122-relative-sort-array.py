class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        L=[]
        L1=[]
        for i in arr2:
            if arr1.count(i)>0: L=L+[i]*arr1.count(i)
        for i in arr1:
            if i not in arr2: L1.append(i)
        L1.sort()
        return L+L1