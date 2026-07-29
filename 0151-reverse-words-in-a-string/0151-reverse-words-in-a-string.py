class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip(" ")
        s=s.split(" ")
        s[:]=s[-1::-1]
        s1=""
        for i in range(len(s)):
            if len(s[i])>0:
                s1+=s[i]+" "
        return s1[:-1]