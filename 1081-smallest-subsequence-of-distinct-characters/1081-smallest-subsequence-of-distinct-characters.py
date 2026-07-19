class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = Counter(s)
        seen = set()
        L = []
        for c in s:
            freq[c] -= 1
            if c in seen: continue
            while L and L[-1] > c and freq[L[-1]]:
                seen.remove(L.pop())
            L.append(c)
            seen.add(c)
        return "".join(L)