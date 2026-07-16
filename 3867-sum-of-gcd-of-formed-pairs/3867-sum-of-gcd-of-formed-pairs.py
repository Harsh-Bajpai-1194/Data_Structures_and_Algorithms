class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        L,sum,maximum=[],0,0
        for i in nums:
            maximum=max(maximum,i)
            L.append(math.gcd(i,maximum))
        L.sort()
        i,j=0,len(nums)-1
        while (j>i):
            sum=sum+math.gcd(L[i],L[j])
            i+=1
            j-=1
        return sum