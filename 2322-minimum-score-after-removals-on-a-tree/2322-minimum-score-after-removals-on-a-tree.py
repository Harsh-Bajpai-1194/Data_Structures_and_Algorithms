class Solution(object):
    def minimumScore(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        n = len(nums)
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        xor = [0] * n
        in_time = [0] * n
        out_time = [0] * n
        parent = [-1] * n
        time = [0]
        def dfs(u, p):
            xor[u] = nums[u]
            parent[u] = p
            time[0] += 1
            in_time[u] = time[0]
            for v in tree[u]:
                if v == p:
                    continue
                dfs(v, u)
                xor[u] ^= xor[v]
            time[0] += 1
            out_time[u] = time[0]
        dfs(0, -1)
        def is_ancestor(u, v):
            return in_time[u] < in_time[v] and out_time[v] < out_time[u]
        min_score = float('inf')
        edge_list = []
        for u, v in edges:
            if parent[v] == u:
                edge_list.append((u, v))  # u->v
            else:
                edge_list.append((v, u))  # v->u
        for i in range(len(edge_list)):
            for j in range(i + 1, len(edge_list)):
                _, a = edge_list[i]
                _, b = edge_list[j]
                if is_ancestor(a, b):
                    x = xor[b]
                    y = xor[a] ^ xor[b]
                    z = xor[0] ^ xor[a]
                elif is_ancestor(b, a):
                    x = xor[a]
                    y = xor[b] ^ xor[a]
                    z = xor[0] ^ xor[b]
                else:
                    x = xor[a]
                    y = xor[b]
                    z = xor[0] ^ xor[a] ^ xor[b]
                max_x = max(x, y, z)
                min_x = min(x, y, z)
                min_score = min(min_score, max_x - min_x)
        return min_score