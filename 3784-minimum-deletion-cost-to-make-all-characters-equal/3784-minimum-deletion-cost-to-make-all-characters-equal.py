class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        a={}
        count=0
        s1=s
        for i,j in enumerate(s1):
            b=cost[i]
            count+=1
            a[j]=b+a.get(j,0)
        if len(a)==0: return 0
        else: 
            c=sum(cost)-max(a.values())
        return c