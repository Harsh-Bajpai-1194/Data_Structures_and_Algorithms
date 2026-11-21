class Solution(object):
    def findSubtreeSizes(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[int]
        """
        from collections import defaultdict
        n = len(s)
        g = defaultdict(list)
        for i in range(1, n):
            g[parent[i]].append(i)
        anc = {}
        def rewire(u):
            c = s[u]
            p = anc.get(c)
            if p is not None and u != 0:
                parent[u] = p
            prev = anc.get(c)
            anc[c] = u
            for v in g[u]:
                rewire(v)
            anc[c] = prev
        rewire(0)
        g2 = defaultdict(list)
        for i in range(1, n):
            g2[parent[i]].append(i)
        ans = [1] * n
        def sz(u):
            for v in g2[u]:
                ans[u] += sz(v)
            return ans[u]
        sz(0)
        return ans