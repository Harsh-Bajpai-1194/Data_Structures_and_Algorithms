class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        import itertools
        a=list(itertools.permutations(digits,3))
        n=len(a)
        c=0
        L=[]
        for i in range(n):
            if a[i][2]%2==0 and a[i][0]!=0:
                L.append(a[i])
        return len(set(L))