class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split()
        s1=[0]*len(s)
        for i in s: s1[int(i[-1])-1]=i[:-1]
        return " ".join(s1)