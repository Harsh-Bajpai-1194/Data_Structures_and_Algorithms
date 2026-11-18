class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adj=[[] for i in range(n+1)]
        for u,v,w in times:
            adj[u].append((v,w))
        dist=[float('inf')]*(n+1)
        dist[k]=0
        def dfs(k,time):
            for ngh , w in adj[k]:
                new=time+w
                if new<dist[ngh]:
                    dist[ngh]=new
                    dfs(ngh,new)
        dfs(k,0)
        print(dist)
        res=max(dist[1:])
        if res!=float('inf'):
            return res
        else:
            return -1