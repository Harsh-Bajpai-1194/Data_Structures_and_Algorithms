class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        exps = []
        i = 0
        temp = n
        while temp:
            if temp & 1:
                exps.append(i)
            i += 1
            temp >>= 1
        pref = [0] * (len(exps) + 1)
        for idx in range(len(exps)):
            pref[idx + 1] = pref[idx] + exps[idx]
        ans = []
        for l, r in queries:
            ans.append(pow(2, pref[r + 1] - pref[l], MOD))
        return ans