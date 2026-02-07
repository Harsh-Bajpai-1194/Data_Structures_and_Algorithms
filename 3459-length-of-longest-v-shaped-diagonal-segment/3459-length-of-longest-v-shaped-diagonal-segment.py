class Solution(object):
    def lenOfVDiagonal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        dirs = [(1,1),(1,-1),(-1,-1),(-1,1)]
        alt2 = [[[0]*m for _ in range(n)] for _ in range(4)]
        alt0 = [[[0]*m for _ in range(n)] for _ in range(4)]
        for k,(di,dj) in enumerate(dirs):
            irange = range(n-1, -1, -1) if di==1 else range(n)
            jrange = range(m-1, -1, -1) if dj==1 else range(m)
            for i in irange:
                for j in jrange:
                    if grid[i][j]==2:
                        ni, nj = i+di, j+dj
                        if 0<=ni<n and 0<=nj<m:
                            alt2[k][i][j] = 1 + alt0[k][ni][nj]
                        else:
                            alt2[k][i][j] = 1
                    elif grid[i][j]==0:
                        ni, nj = i+di, j+dj
                        if 0<=ni<n and 0<=nj<m:
                            alt0[k][i][j] = 1 + alt2[k][ni][nj]
                        else:
                            alt0[k][i][j] = 1
        ans = 0
        for row in grid:
            if 1 in row:
                ans = 1
                break
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 1:
                    continue
                for k,(di,dj) in enumerate(dirs):
                    ni, nj = i+di, j+dj
                    if not (0<=ni<n and 0<=nj<m):
                        continue
                    if grid[ni][nj] != 2:
                        continue
                    L = alt2[k][ni][nj]
                    if 1 + L > ans:
                        ans = 1 + L
                    pi, pj = ni, nj
                    parity = 0
                    cwk = (k+1) % 4
                    cwdi, cwdj = dirs[cwk]
                    for t in range(L):
                        tx, ty = pi + cwdi, pj + cwdj
                        cont = 0
                        if 0<=tx<n and 0<=ty<m:
                            if parity==0:
                                cont = alt0[cwk][tx][ty]
                            else:
                                cont = alt2[cwk][tx][ty]
                        total = 1 + (t+1) + cont
                        if total > ans:
                            ans = total
                        pi += di; pj += dj
                        parity ^= 1
        return ans