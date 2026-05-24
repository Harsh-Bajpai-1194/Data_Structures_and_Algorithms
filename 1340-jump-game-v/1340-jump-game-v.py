class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        seen = dict()
        def dfs(j):
            if j in seen: return
            seen[j] = 1
            i = j - 1
            while i >= 0 and j - i <= d and arr[j] > arr[i]:
                dfs(i)
                seen[j] = max(seen[j], seen[i] + 1)
                i -= 1
            i = j + 1
            while i < len(arr) and i - j <= d and arr[j] > arr[i]:
                dfs(i)
                seen[j] = max(seen[j], seen[i] + 1)
                i += 1
        for i in range(len(arr)): dfs(i)
        return max(seen.values())