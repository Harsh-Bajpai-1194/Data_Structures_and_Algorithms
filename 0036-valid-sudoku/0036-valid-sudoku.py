class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    continue
                b = (r // 3) * 3 + (c // 3)
                if ch in rows[r] or ch in cols[c] or ch in boxes[b]:
                    return False
                rows[r].add(ch)
                cols[c].add(ch)
                boxes[b].add(ch)
        return True