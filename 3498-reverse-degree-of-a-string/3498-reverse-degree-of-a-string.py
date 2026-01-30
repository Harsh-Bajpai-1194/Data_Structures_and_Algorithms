class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=0
        for i in range(len(s)): n+=(123-ord(s[i]))*(i+1)
        return n