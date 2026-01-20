class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count=0
        s=str(num)
        for i in range(len(s)):
            if num%int(s[i])==0:
                count+=1
        return count