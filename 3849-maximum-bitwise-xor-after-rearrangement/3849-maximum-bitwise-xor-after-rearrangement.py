class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        L=(s,t)
        zero=t.count("0")
        one=len(t)-zero
        L1=[]
        for i in s:
            if i=="0":
                if one>0:
                    L1.append("1")
                    one=one-1
                else: 
                    L1.append("0")
                    zero=zero-1
            else:
                if zero>0:
                    L1.append("1")
                    zero=zero-1
                else: 
                    L1.append("0")
                    one=one-1
        L="".join(L1)
        return L