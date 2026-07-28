class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s)==1: return s
        s1=""
        s=sorted(s)
        s=s[-1::-1]
        if len(s)%2==1 and len(s)>1:
            character='a'
            for i in range(26):
                if s.count(character)%2!=0:
                    s1=character
                    break
                character=ord(character)+1
                character=chr(character)
            s="".join(s)
            s=s.replace(s1[0],"",1)
            for i in range(len(s)):
                if i%2==0: s1=s1+s[i]
                else: s1=s[i]+s1
        else:
            for i in range(len(s)):
                if i%2==0: s1=s1+s[i]
                else: s1=s[i]+s1
        return s1