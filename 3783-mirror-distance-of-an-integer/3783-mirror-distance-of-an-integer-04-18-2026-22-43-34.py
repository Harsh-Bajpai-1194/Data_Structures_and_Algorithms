class Solution:
    def mirrorDistance(self, n: int) -> int:
        a=int(str(n)[-1::-1])
        return abs(n-a)