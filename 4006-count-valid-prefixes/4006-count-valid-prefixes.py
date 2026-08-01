class Solution:
    def countValidPrefixes(self, s: str) -> int:
        c,zero,one=0,0,0
        for i in s:
            if i=='0': zero+=1
            else: one+=1
            if abs(zero-one)<2: c+=1
        return c