class Solution:
    def longestBalanced(self, s: str) -> int:
        n,res=len(s),0
        for i in range(n):
            c = defaultdict(int)
            for j in range(i, n):
                c[s[j]] += 1
                if len(set(c.values())) == 1:
                    res = max(res, j - i + 1)
        return res