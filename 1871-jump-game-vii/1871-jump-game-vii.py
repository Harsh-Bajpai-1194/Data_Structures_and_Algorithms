class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        L, L1 = [0] * n, [0] * n
        L[0] = 1
        for i in range(minJump):
            L1[i] = 1
        for i in range(minJump, n):
            left, right = i - maxJump, i - minJump
            if s[i] == "0":
                if left>0:
                    total = L1[right] - L1[left - 1]
                else:
                    total = L1[right]
                L[i] = int(total != 0)
            L1[i] = L1[i - 1] + L[i]
        return bool(L[n - 1])