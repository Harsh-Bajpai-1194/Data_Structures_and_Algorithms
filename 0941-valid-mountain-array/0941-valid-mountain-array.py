class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr)<3 or arr[0]>arr[1] or arr[-1]>arr[-2]: return False
        index=None
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]: 
                index=i
                break
            if arr[i]==arr[i+1]: return False
        if index==None: return False
        for i in range(index,len(arr)-1):
            if arr[i]<=arr[i+1]: return False
        return True