class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px = find(x)
            py = find(y)
            if px < py:
                parent[py] = px
            else:
                parent[px] = py
        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))
        result = []
        for c in baseStr:
            rep = find(ord(c) - ord('a'))
            result.append(chr(rep + ord('a')))
        return ''.join(result)