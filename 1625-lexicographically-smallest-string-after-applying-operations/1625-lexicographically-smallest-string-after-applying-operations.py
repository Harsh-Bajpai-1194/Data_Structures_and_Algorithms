class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        from collections import deque
        visited = set()
        q = deque([s])
        res = s
        while q:
            curr = q.popleft()
            res = min(res, curr)
            added = list(curr)
            for i in range(1, len(added), 2):
                added[i] = str((int(added[i]) + a) % 10)
            added_str = ''.join(added)
            if added_str not in visited:
                visited.add(added_str)
                q.append(added_str)
            rotated = curr[-b:] + curr[:-b]
            if rotated not in visited:
                visited.add(rotated)
                q.append(rotated)
        return res