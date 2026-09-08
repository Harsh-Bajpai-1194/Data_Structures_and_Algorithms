class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000: return 0
        elif n==1000: return 1
        c=0
        for i in range(1000,n+1):
            a=len(str(i))-1
            c=c+a//3
        return c