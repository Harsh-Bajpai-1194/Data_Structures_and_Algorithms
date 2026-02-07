class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if len(s)==2: return True if s[0]==s[1] else False
        s1=""
        for i in range(len(s)-1):
            s1+=str((int(s[i])+int(s[i+1]))%10)
        return self.hasSameDigits(s1)