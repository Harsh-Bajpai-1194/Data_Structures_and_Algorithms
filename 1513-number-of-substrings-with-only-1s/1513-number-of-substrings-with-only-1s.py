class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        count = 0
        mod = 10**9 + 7
        for char in s:
            if char == '1':
                count += 1
                res = (res + count) % mod
            else: count = 0
        return res