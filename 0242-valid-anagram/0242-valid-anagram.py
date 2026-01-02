class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (s==t): return True
        if (len(s)!=len(t)): return False
        a,b=list(s),list(t)
        for i in a:
            if i in b:
                b.remove(i)
            else:
                return False
        return True