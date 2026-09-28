class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        e=len(connections)
        if (e<n-1): return -1
        adj=[[] for i in range(n)]
        for x, y in connections:
            adj[x].append(y)
            adj[y].append(x)
        visited=[0]*n
        count=0
        for i in range(n):
            if (visited[i]==0):
                q=[i]
                visited[i]=1
                count+=1
                while(q):
                    node=q.pop()
                    for neighbor in adj[node]:
                        if visited[neighbor]==0:
                            visited[neighbor]=1
                            q.append(neighbor)
        return count-1