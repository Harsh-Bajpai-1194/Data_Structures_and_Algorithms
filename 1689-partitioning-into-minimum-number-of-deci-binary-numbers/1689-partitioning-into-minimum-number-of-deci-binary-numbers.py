class Solution:
    def minPartitions(self, n: str) -> int:
        return int(sorted(n)[-1])