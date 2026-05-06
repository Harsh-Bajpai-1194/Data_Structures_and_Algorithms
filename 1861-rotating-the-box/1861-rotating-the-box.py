class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])
        result = [["" for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                result[i][j] = boxGrid[j][i]
        for i in range(n):
            result[i].reverse()
        for j in range(m):
            for i in range(n - 1, -1, -1):
                if (result[i][j] == "."):
                    next_row_with_stone = -1
                    for k in range(i - 1, -1, -1):
                        if result[k][j] == "*":
                            break  
                        if result[k][j] == "#": 
                            next_row_with_stone = k
                            break
                    if next_row_with_stone != -1:
                        result[next_row_with_stone][j] = "."
                        result[i][j] = "#"
        return result