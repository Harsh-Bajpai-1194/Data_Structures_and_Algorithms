class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        L = [[] for i in range(n)]
        L1 = defaultdict(int)
        for i in range(n):
            L[i] = [i]
        for v1, v2 in edges:
            L[v1].append(v2)
            L[v2].append(v1)
        for i in range(n):
            neighbors = tuple(sorted(L[i]))
            L1[neighbors] += 1
        return sum(1 for neighbors, freq in L1.items() if len(neighbors) == freq)