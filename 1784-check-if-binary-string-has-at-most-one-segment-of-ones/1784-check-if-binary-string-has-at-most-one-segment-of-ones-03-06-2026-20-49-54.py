class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return True if len(set(s[:s.count("1")]))==1 else False