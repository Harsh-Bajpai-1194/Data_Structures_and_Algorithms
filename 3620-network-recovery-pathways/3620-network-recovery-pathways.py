class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n, ans = len(online), -1
        g, ind = [[] for i in range(n)], [0] * n
        for u, v, w in edges: g[u].append((v, w)); ind[v] += 1
        q = [i for i in range(n) if not ind[i]]
        for u in q:
            for v, j in g[u]:
                ind[v] -= 1
                if not ind[v]: q.append(v)
        l, r = 0, 10**9
        while l <= r:
            m, dp = (l + r) // 2, [0] + [1e30] * (n - 1)
            for u in q:
                if dp[u] < 1e30 and (not u or u == n-1 or online[u]):
                    for v, w in g[u]:
                        if w >= m and (v == n-1 or online[v]): dp[v] = min(dp[v], dp[u] + w)
            if dp[-1] <= k: ans, l = m, m + 1
            else: r = m - 1
        return ans