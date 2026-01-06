class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n==1: return [0]
        if n==2: return [-1,1]
        L=[]
        for i in range(n-1):
            L.append(i)
        L.insert(0,-sum(L))
        return L