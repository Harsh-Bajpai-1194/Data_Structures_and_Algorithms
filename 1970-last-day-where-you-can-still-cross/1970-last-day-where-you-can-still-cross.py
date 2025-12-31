class Solution(object):
    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """
        import collections
        left, right = 1, len(cells)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            grid = [[0] * col for i in range(row)]
            for i in range(mid):
                r, c = cells[i]
                grid[r-1][c-1] = 1
            q = collections.deque()
            for c in range(col):
                if grid[0][c] == 0:
                    q.append((0, c))
                    grid[0][c] = 1
            can_cross = False
            while q:
                r, c = q.popleft()
                if r == row - 1:
                    can_cross = True
                    break
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr, nc))
            if can_cross:
                ans = mid
                left = mid + 1
            else: right = mid - 1
        return ans