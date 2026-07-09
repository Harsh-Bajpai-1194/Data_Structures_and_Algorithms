class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        L=[0]*n
        for i in range(1, n):
            if nums[i]-nums[i-1]<=maxDiff: L[i]=L[i-1]
            else: L[i]=L[i-1]+1
        L1=[]
        for u,v in queries: L1.append(L[u]==L[v])
        return L1