class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        L=[]
        for i in nums:
            if nums.count(i)==1:
                L.append(i)
        s=0
        for i in L:
            s+=i
        return s