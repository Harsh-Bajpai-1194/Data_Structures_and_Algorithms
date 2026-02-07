class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=""  
        for c in s:  
            if'a'<=c<='z': l+=c  
            elif c=='*'and l: l=l[:-1]  
            elif c=='#': l+=l  
            elif c=='%': l=l[::-1]  
        return l