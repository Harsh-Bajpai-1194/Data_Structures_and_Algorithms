class Solution:
    def minMoves(self, classroom, energy):
        from collections import deque
        m, n = len(classroom), len(classroom[0])
        sr, sc, cnt = -1, -1, 0
        id = [[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S': sr, sc = i, j
                elif classroom[i][j] == 'L':
                    id[i][j] = cnt
                    cnt += 1
        fullMask = (1 << cnt) - 1
        best = [[[-1] * (1 << cnt) for _ in range(n)] for _ in range(m)]
        q = deque([(sr, sc, 0, energy, 0)])
        best[sr][sc][0] = energy
        while q:
            r, c, mask, en, dist = q.popleft()
            if mask == fullMask: return dist
            if not en: continue
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    newMask = mask | (1 << id[nr][nc]) if classroom[nr][nc] == 'L' else mask
                    newEn = energy if classroom[nr][nc] == 'R' else en - 1
                    if best[nr][nc][newMask] < newEn:
                        best[nr][nc][newMask] = newEn
                        q.append((nr, nc, newMask, newEn, dist + 1))
        return -1