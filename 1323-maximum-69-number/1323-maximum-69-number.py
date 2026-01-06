class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        s=str(num) 
        s=s.replace('6', '9', 1)  
        return int(s)