import collections
from sortedcontainers import SortedDict
class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        count = collections.Counter(nums)
        line = SortedDict()
        for num in nums:
            start = num - k
            end = num + k + 1
            line[start] = line.get(start, 0) + 1
            line[end] = line.get(end, 0) - 1
        ans = 0
        adjustable = 0 
        all_critical_points = sorted(set(line.keys()) | set(count.keys()))
        for x in all_critical_points:
            adjustable += line.get(x, 0)
            n_A = count.get(x, 0)
            n_B = adjustable - n_A
            current_freq = n_A + min(numOperations, n_B)
            ans = max(ans, current_freq)
        return ans