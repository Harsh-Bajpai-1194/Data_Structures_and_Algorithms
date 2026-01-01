class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=""
        L=[]
        for i in digits: s+=str(i)
        s=str(int(s)+1)
        for i in range(len(s)): L.append(int(s[i]))
        return L