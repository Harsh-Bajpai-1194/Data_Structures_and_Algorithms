class Solution:
    def pacificAtlantic(self,h:List[List[int]])->List[List[int]]:
        m,n=len(h),len(h[0]);d=[(1,0),(-1,0),(0,1),(0,-1)]
        def f(r,c,v):
            if (r,c)in v: return
            v.add((r,c));[f(r+dr,c+dc,v)for dr,dc in d if 0<=r+dr<m and 0<=c+dc<n and h[r+dr][c+dc]>=h[r][c]]
        P,A=set(),set();[f(i,0,P) or f(i,n-1,A)for i in range(m)];[f(0,j,P)or f(m-1,j,A)for j in range(n)]
        return list(map(list,P&A))