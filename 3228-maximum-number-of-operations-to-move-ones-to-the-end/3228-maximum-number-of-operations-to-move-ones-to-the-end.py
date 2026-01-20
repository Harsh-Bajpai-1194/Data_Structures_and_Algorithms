class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        ops = ones_count = 0        
        for i in range(n):
            if s[i] == '1': ones_count += 1
            elif i > 0 and s[i-1] == '1': ops += ones_count
        return ops