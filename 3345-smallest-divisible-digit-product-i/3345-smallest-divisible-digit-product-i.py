class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,n+t):
            prod=1
            for j in range(len(str(i))):
                prod*=int(str(i)[j])
            if prod%t==0: return i