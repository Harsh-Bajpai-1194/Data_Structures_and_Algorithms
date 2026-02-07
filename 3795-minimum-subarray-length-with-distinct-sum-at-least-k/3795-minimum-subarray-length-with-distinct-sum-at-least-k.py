class Solution(object):
    def minLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        minimum=float('inf')
        sum=i=0
        count=defaultdict(int)
        for j in range(len(nums)):
            a=nums[j]
            count[a]+=1
            if count[a]==1: 
                sum=sum+a
            while (sum>=k):
                minimum=min(minimum,j-i+1)
                b=nums[i]
                count[b]-=1
                if count[b]==0: 
                    sum=sum-b
                i+=1
        if (minimum!=float('inf')): return minimum 
        else: return -1