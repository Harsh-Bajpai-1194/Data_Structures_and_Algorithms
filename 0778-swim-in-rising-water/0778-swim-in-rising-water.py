from heapq import heappush, heappop
class Solution:
    def swimInWater(self,g:List[List[int]])->int:
        n=len(g);v=[[0]*n for _ in range(n)];h=[(g[0][0],0,0)];v[0][0]=1;r=0
        while h:
            t,x,y=heappop(h);r=max(r,t)
            if x==y==n-1:return r
            for dx,dy in[(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<n and not v[nx][ny]:v[nx][ny]=1;heappush(h,(g[nx][ny],nx,ny))