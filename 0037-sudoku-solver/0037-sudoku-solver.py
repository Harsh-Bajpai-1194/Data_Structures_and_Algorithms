class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]
        empties=[]
        
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    empties.append((i,j))
                else:
                    ch=board[i][j]
                    rows[i].add(ch)
                    cols[j].add(ch)
                    boxes[(i//3)*3+j//3].add(ch)
        
        def backtrack(k=0):
            if k==len(empties): return True
            r,c=empties[k]
            b=(r//3)*3+c//3
            for ch in map(str,range(1,10)):
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[b]:
                    board[r][c]=ch
                    rows[r].add(ch); cols[c].add(ch); boxes[b].add(ch)
                    if backtrack(k+1): return True
                    board[r][c]="."
                    rows[r].remove(ch); cols[c].remove(ch); boxes[b].remove(ch)
            return False
        
        backtrack()