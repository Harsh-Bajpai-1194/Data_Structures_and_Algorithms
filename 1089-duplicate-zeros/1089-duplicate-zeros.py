class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n=len(arr)
        L=[]
        for i in range(n):
            if arr[i]==0:
                L.append(i)
        c=0
        for i in L:
            arr.insert(i+c,7777777)
            c+=1
        for i in range(n):
            if arr[i]==7777777:
                arr[i]=0
        arr[:]=arr[:n]