class Solution(object):
    def resultingString(self, s):
        """
        :type s: str
        :rtype: str
        """
        L=[]
        for i in s:
            if L:
                a=L[-1]
                flag=False
                if abs(ord(a)-ord(i))==1:
                    flag=True
                elif (a=='a' and i=='z') or (a=='z' and i=='a'):
                    flag=True
                if flag:
                    L.pop()
                else:
                    L.append(i)
            else:
                L.append(i)
        L1="".join(L)
        return L1