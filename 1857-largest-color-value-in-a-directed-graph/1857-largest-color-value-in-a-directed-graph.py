class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        from collections import defaultdict, deque
        n = len(colors)
        graph = defaultdict(list)
        in_degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        dp = [[0] * 26 for _ in range(n)]
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        visited = 0
        max_color_val = 0
        while queue:
            node = queue.popleft()
            visited += 1
            color_index = ord(colors[node]) - ord('a')
            dp[node][color_index] += 1
            max_color_val = max(max_color_val, dp[node][color_index])
            for neighbor in graph[node]:
                for c in range(26):
                    dp[neighbor][c] = max(dp[neighbor][c], dp[node][c])
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return max_color_val if visited == n else -1