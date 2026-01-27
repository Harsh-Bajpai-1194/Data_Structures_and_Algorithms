class Solution(object):
    def minCost(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[] for i in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))
        pq = [(0, 0)]
        min_costs = {0: 0}
        while pq:
            cost, u = heapq.heappop(pq)
            if u == n-1:return cost
            if cost > min_costs.get(u, float('inf')): continue
            for v, weight in graph[u]:
                new_cost = cost + weight
                if new_cost < min_costs.get(v, float('inf')):
                    min_costs[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))   
        return -1