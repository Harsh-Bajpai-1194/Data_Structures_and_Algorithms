class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        L=[]
        L1=[]
        for i in range(len(nums)):
            L.append(i+1)
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                L1.append(nums[i])
                break
        nums=list(set(nums))
        nums.sort()
        for i in range(min(len(L),len(nums))):
            if L[i]!=nums[i]:
                L1.append(L[i])
                break
        return L1 if len(L1)==2 else L1+[len(L)]