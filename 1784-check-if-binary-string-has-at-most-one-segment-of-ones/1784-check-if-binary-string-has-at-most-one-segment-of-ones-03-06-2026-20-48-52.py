class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        s1=s[:s.count("1")]
        if len(set(s1))==1: return True
        return False