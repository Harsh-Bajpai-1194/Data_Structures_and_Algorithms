class Solution:
    def minJumps(self, arr: List[int]) -> int:
        graph = {}
        for i, j in enumerate(arr):
            graph.setdefault(j, []).append(i)
        current, visited, step = [0], {0}, 0
        while current:
            nex = []
            for i in current:
                if i == len(arr) - 1: return step
                for child in graph[arr[i]] + [i - 1, i + 1]:
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)
                graph[arr[i]].clear()
            current, step = nex, step + 1
        return -1