class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :type k: int
        :rtype: int
        """
        import sys
        sys.setrecursionlimit(100000)
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        self.ans = 0
        def dfs(node, parent):
            s = values[node]
            for child in adj[node]:
                if child != parent: s += dfs(child, node)
            if s % k == 0:
                self.ans += 1
                return 0
            return s
        dfs(0, -1)
        return self.ans