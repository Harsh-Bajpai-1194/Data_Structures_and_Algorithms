class Solution(object):
    def sumOfLargestPrimes(self, s):
        """
        :type s: str
        :rtype: int
        """
        prime_num=set()
        for i in range(len(s)):
            num=0
            for j in range(i,len(s)):
                num=num*10+int(s[j])
                if num<2:
                    continue
                flag=True
                for k in range(2,int(sqrt(num))+1):
                    if num%k==0:
                        flag=False
                        break
                if flag==True:
                    prime_num.add(num)
        largest=sorted(prime_num,reverse=True)
        L=largest[:3]
        return sum(L)