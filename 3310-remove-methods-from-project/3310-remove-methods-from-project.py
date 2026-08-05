class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        L = [[] for i in range(n)]
        L1 = [0] * n
        for u, v in invocations:
            L[u].append(v)
            L1[v] += 1
        queue = collections.deque([k])
        L2 = bytearray(n)
        L2[k] = 1
        while queue:
            u = queue.popleft()
            for v in L[u]:
                L1[v] -= 1
                if L2[v] == 0:
                    queue.append(v)
                    L2[v] = 1
        can_remove_all = True
        for i in range(n):
            if L2[i] == 1 and L1[i] > 0:
                can_remove_all = False
                break
        if not can_remove_all: return list(range(n))
        return [i for i in range(n) if L2[i] == 0]