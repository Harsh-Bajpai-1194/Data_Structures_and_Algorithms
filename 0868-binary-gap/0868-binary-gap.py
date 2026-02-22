class Solution:
    def binaryGap(self, n: int) -> int:
        a=bin(n)[2:]
        L=[a.index("1")]
        for i in range(L[0]+1,len(a)): 
            if a[i]=="1": L.append(i)
        if len(L)==1: return 0
        if len(L)==2: return L[1]-L[0]
        else:
            maximum=0
            for i in range(len(L)-1):
                maximum=max(maximum,L[i+1]-L[i])
            return maximum