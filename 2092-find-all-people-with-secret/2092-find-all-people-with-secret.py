class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        from collections import defaultdict, deque
        known = {0, firstPerson}
        meetings.sort(key=lambda x: x[2])
        i = 0
        m = len(meetings)
        while i < m:
            j = i
            curr_time = meetings[i][2]
            while j < m and meetings[j][2] == curr_time: j += 1
            adj = defaultdict(list)
            involved = set()
            for k in range(i, j):
                u, v, _ = meetings[k]
                adj[u].append(v)
                adj[v].append(u)
                involved.add(u)
                involved.add(v)
            queue = deque([p for p in involved if p in known])
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if v not in known:
                        known.add(v)
                        queue.append(v)
            i = j
        return list(known)