class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n,V,C=len(items),[sum(1 for j in range(len(items)) if items[j][0]%items[i][0]==0) for i in range(len(items))],[i[1] for i in items]
        a,b=min(C),sum(V)
        dp=[0]+[-1]*budget
        for i,j in zip(V,C):
            for k in range(budget,j-1,-1):
                if dp[k-j]!=-1:
                    dp[k]=max(dp[k],dp[k-j]+i)
        result=0
        for i in range(budget+1):
            if dp[i]!=-1:
                value=dp[i]+(budget-i)//a
                result=max(result,value)
        return result