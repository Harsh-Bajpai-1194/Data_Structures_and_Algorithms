class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        server, time = zip(*sorted(logs, key=itemgetter(1)), [0, inf])  
        cnt = [0] * (n + 1) 
        busy = lo = hi = 0
        ans = [0] * len(queries)
        for i, q in sorted(enumerate(queries), key=itemgetter(1)):
            while time[hi] <= q:  
                busy += not cnt[server[hi]]
                cnt[server[hi]] += 1
                hi += 1
            while time[lo] < q - x: 
                cnt[server[lo]] -= 1
                busy -= not cnt[server[lo]]
                lo += 1
            ans[i] = n - busy
        return ans