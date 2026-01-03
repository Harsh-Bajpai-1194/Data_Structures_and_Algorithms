class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s1=""
        while(len(s1)!=len(s)):
            for i in range(0,len(s),k):
                if i%(k*2)==0: s1+=s[i:i+k][-1::-1]
                else: s1+=s[i:i+k]
        return s1