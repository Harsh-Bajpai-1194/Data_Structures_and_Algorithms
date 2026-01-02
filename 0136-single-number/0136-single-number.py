class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        L=[nums[0]]
        for i in nums:
            if i not in L:
                L.append(i)
        for i in L:
            if nums.count(i)==1: return i