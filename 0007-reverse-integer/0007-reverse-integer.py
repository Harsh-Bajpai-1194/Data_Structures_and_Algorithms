class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sum=0
        c=0
        if x<0: c=1
        x=abs(x)
        while (x!=0):
            if (sum>(pow(2,31)-1)/10 or sum<-pow(2,31)/10): return 0 
            else:
                sum=sum*10+x%10
                x//=10
        return sum*(-1)**c