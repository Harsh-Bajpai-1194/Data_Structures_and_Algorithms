class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        L=[]
        for i in range(len(s)-1):
            for j in range(i,len(s)):
                L.append(s[i:j+1])
        L+=s[-1]
        for i in L:
            for j in i:
                flag=True
                if i.count(j)>2: 
                    flag=False
                    break
            if flag: c=max(c,len(i))
        return c