class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        :type m: int
        :type n: int
        :type hFences: List[int]
        :type vFences: List[int]
        :rtype: int
        """
        hFences.append(1)
        hFences.append(m)
        vFences.append(1)
        vFences.append(n)
        hFences.sort()
        vFences.sort()
        h_distances = set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                h_distances.add(hFences[j] - hFences[i])
        max_side = -1
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                diff = vFences[j] - vFences[i]
                if diff in h_distances:
                    max_side = max(max_side, diff)
        if max_side == -1: return -1
        return (max_side * max_side) % (10**9 + 7)