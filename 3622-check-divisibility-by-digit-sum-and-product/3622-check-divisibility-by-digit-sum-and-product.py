class Solution:
    def checkDivisibility(self, n: int) -> bool:
        a=str(n)
        sum,prod=0,1
        for i in range(len(a)):
            sum+=int(a[i])
            prod*=int(a[i])
        return n%(sum+prod)==0