class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=bin(n)[2:]
        s=(32-len(a))*"0"+a
        s=s[-1::-1]
        return int(s,2)