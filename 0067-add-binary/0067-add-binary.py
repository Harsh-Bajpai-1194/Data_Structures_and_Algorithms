class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a="0b"+a
        b="0b"+b
        sum=int(a,2)+int(b,2)
        return bin(sum)[2:]