class Solution(object):
    def decimalRepresentation(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        i=0
        L=[]
        while(n!=0):
            a=(n%10)*pow(10,i)
            i+=1
            L.append(a)
            n//=10
        L.reverse()
        zeros=L.count(0)
        for i in range(zeros): L.remove(0)
        return L