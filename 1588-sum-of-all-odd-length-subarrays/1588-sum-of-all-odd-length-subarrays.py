class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        L=[]
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if len(arr[i:j+1])%2==1: L.append(arr[i:j+1])
        sum1=0
        for i in L:
            sum1+=sum(i)
        return sum1