class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        a=list(set(s))
        if len(a)==1: 
            if a[0]=="z": return 1
            if a[0]=="a": return 0
            else: return 26-(ord(s[0])-ord('a'))
        s=list(s)
        s.sort()
        s=",".join(s)
        s=s.replace(",","")
        for i in range(len(s)-1):
            if s[i]!="a" and s[i]!="z" and s[i]!=s[i+1]: 
                count+=ord(s[i+1])-ord(s[i])
                s=s.replace(s[i],s[i+1])
        count+=ord('z')-ord(s[-1])
        s=s.replace(s[-1],'z')
        return count+1