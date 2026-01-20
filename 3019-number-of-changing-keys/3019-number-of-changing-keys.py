class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=s.lower()
        count=0
        for i in range(1,len(a)):
            if a[i]!=a[i-1]:
                count+=1
        return count