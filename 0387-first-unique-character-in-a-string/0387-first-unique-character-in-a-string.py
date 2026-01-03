class Solution:
    def firstUniqChar(self, s: str) -> int:
        a=[]
        for i in s:
            if i not in a:
                a.append(i)
        for i in a:
            if s.count(i)==1: return s.index(i)
        return -1