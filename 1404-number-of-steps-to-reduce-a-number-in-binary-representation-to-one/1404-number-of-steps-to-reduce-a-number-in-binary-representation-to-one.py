class Solution:
    def numSteps(self, s: str) -> int:
        a=int(s,2)
        c=0
        while (a!=1):
            if a%2==0: a//=2
            else: a+=1
            c+=1
        return c