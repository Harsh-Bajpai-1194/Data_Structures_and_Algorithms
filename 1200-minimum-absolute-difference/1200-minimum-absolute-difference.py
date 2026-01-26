class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        d=float('inf')
        for i in range(len(arr)-1):
            d=min(d,arr[i+1]-arr[i])
        L=[]
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == d: L.append([arr[i], arr[i+1]])
        return L