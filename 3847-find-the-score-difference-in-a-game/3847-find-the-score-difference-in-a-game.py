class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        a,b,active=0,0,0
        for i in range(len(nums)):
            if nums[i]%2!=0: active=1-active
            if (i+1)%6==0: active=1-active
            if active==0: a+=nums[i]
            else: b+=nums[i]
        return a-b