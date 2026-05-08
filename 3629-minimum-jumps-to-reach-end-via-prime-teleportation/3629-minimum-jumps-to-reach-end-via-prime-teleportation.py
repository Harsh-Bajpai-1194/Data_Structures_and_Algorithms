MAXV = 1000001
spf = list(range(MAXV))
for i in range(2, 1001):
    if spf[i] == i:
        for j in range(i*i, MAXV, i):
            if spf[j] == j: spf[j] = i
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n, maxi = len(nums), max(nums)
        if n == 1: return 0
        primes_in_nums = {x for x in nums if x >= 2 and spf[x] == x}
        mp = defaultdict(list)
        for i, x in enumerate(nums):
            while x > 1:
                p = spf[x]
                if p in primes_in_nums: mp[p].append(i)
                while x % p == 0: x //= p
        dist = {0: 0}
        q, used_p = deque([0]), set()
        while q:
            u = q.popleft()
            d = dist[u] + 1
            neighbors = [u - 1, u + 1]
            val = nums[u]
            if val in primes_in_nums and val not in used_p:
                neighbors += mp[val]
                used_p.add(val)
            for v in neighbors:
                if 0 <= v < n and v not in dist:
                    if v == n - 1: return d
                    dist[v] = d
                    q.append(v)
        return -1