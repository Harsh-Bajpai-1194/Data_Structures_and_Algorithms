class Solution(object):
    def largestEven(self, s):
        """
        :type s: str
        :rtype: str
        """
        while(s!="0"):
            if int(s)%2==0: return s
            else: s=str(int(s)//10)
        return ""