class Solution(object):
    def getLeastFrequentDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if len(str(n))==1: return n
        n=str(n)
        a=list(set(list(n)))
        least,result=len(n),10
        for i in a:
            c=n.count(i)
            if c<least or (c==least and int(i)<result): least,result=c,int(i)
        return result