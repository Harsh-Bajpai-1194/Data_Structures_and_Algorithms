class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict
        parent = list(range(c + 1))
        def find(i):
            if parent[i] == i: return i
            parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j: parent[root_i] = root_j
        for u, v in connections:
            union(u, v)
        components = defaultdict(list)
        for i in range(1, c + 1):
            root = find(i)
            components[root].append(i)    
        results = []
        offline = set()
        smallest_online_index = defaultdict(int)
        for query_type, x in queries:
            if query_type == 2: offline.add(x)
            else:
                if x not in offline: results.append(x)
                else:
                    root = find(x)
                    members = components[root]
                    idx = smallest_online_index[root]
                    while idx < len(members) and members[idx] in offline: idx += 1
                    smallest_online_index[root] = idx
                    if idx == len(members): results.append(-1)
                    else: results.append(members[idx])          
        return results