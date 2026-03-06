class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if s.count("1")==len(s): return True
        s1=s[:s.count("1")]
        if len(set(s1))==1: return True
        return False