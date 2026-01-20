class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        answer=-1
        for i in range(len(num)-2):
            if num[i]==num[i+1] and num[i]==num[i+2]:
                if int(num[i]+num[i+1]+num[i+2])>=answer:
                    answer=int(num[i]+num[i+1]+num[i+2])
        if answer==-1:
            answer=""
        if answer==0:
            answer="000"
        return str(answer)