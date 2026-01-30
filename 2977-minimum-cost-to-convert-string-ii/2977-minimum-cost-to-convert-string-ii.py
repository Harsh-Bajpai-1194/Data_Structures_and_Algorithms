class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        INF = float('inf')
        n = len(source)
        trie = [[-1] * 26]
        tag = [-1]
        def insert(word):
            node = 0
            for char in word:
                idx = ord(char) - 97
                if trie[node][idx] == -1:
                    trie[node][idx] = len(trie)
                    trie.append([-1] * 26)
                    tag.append(-1)
                node = trie[node][idx]
            if tag[node] == -1:
                tag[node] = next_id[0]
                next_id[0] += 1
            return tag[node]
        next_id = [0]
        parsed_edges = []
        for o, c, w in zip(original, changed, cost):
            u = insert(o)
            v = insert(c)
            parsed_edges.append((u, v, w))
        num_nodes = next_id[0]
        dist = [[INF] * num_nodes for _ in range(num_nodes)]
        for i in range(num_nodes):
            dist[i][i] = 0
        for u, v, w in parsed_edges:
            if w < dist[u][v]:
                dist[u][v] = w
        for k in range(num_nodes):
            for i in range(num_nodes):
                if dist[i][k] == INF: continue
                for j in range(num_nodes):
                    if dist[k][j] == INF: continue
                    new_dist = dist[i][k] + dist[k][j]
                    if new_dist < dist[i][j]:
                        dist[i][j] = new_dist
        s_nums = [ord(c) - 97 for c in source]
        t_nums = [ord(c) - 97 for c in target]
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if dp[i] == INF:
                continue
            if s_nums[i] == t_nums[i]:
                if dp[i] < dp[i+1]:
                    dp[i+1] = dp[i]
            u,v=0,0
            for j in range(i, n):
                u = trie[u][s_nums[j]]
                if u == -1: break
                v = trie[v][t_nums[j]]
                if v == -1: break
                id_u = tag[u]
                id_v = tag[v]
                if id_u != -1 and id_v != -1:
                    w = dist[id_u][id_v]
                    if w != INF:
                        if dp[i] + w < dp[j+1]:
                            dp[j+1] = dp[i] + w
        ans = dp[n]
        return -1 if ans == INF else ans