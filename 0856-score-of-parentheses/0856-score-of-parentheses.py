class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        def F(i, j):
            res=0 
            balance=0
            start=i
            for k in range(start, j):
                balance+=1 if s[k]=='(' else -1
                if balance == 0:
                    if k-start==1: res+=1
                    else: res+=2*F(start+1, k)
                    start = k+1
            return res
        return F(0,len(s))