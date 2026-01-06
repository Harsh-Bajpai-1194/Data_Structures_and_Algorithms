class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count=0
        while(num!=0):
            if num%2==0:
                num=num//2
                count=count+1
            else:
                num=num-1
                count=count+1
        return count