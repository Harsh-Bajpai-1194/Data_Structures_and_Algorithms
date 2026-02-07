class Solution(object):
    def minimumCost(self, s, t, flipCost, swapCost, crossCost):
        """
        :type s: str
        :type t: str
        :type flipCost: int
        :type swapCost: int
        :type crossCost: int
        :rtype: int
        """
        cost=a=b=0
        for i in range(len(s)):
            if s[i]!=t[i]: 
                if s[i]!="0": a=a+1
                else: b=b+1
        total=0
        if a<b: c=a
        else: c=b
        if swapCost<2*flipCost: d=swapCost
        else: d=2*flipCost
        cost=cost+c*d
        difference=abs(a-b)
        if (crossCost+swapCost<2*flipCost): d=crossCost+swapCost
        else: d=2*flipCost
        cost=cost+(difference//2)*d
        if difference%2==1:
            cost=cost+flipCost
        return cost