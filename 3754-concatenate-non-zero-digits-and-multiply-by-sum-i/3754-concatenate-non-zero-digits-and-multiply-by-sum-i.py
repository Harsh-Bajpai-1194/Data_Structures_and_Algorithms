class Solution:
    def sumAndMultiply(self, n: int) -> int:
        L=[int(i) for i in str(n) if i!='0']
        x=int(''.join(map(str,L))) if L else 0
        return sum(L)*x