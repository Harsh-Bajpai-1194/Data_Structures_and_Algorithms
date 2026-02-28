class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result=0
        for i in range(1, n+1):
            result=((result<<i.bit_length())+i)%(10**9+7)
        return result