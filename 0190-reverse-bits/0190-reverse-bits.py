class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=bin(n)[2:]
        b=len(a)
        s=(32-b)*"0"+a
        s=s[-1::-1]
        e=int(s,2)
        return e