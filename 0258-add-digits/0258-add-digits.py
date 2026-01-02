class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        i,sum=1,0
        while(sum>9 or i):
            sum=0
            while(num!=0):
                sum+=num%10
                num//=10
            if (sum<10): return sum
            else: num=sum