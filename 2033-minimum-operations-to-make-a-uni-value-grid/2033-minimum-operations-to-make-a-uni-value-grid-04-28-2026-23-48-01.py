class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        L = []
        a = 0
        for i in grid:
            for num in i:
                L.append(num)
        L.sort()
        b = L[len(L) // 2]
        for i in L:
            if i % x != b % x: return -1
            a += abs(b - i) // x
        return a