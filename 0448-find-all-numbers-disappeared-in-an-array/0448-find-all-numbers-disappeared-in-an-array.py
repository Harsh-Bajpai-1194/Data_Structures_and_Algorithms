class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]: 
        L1=[]
        a=set(nums)
        for i in range(1,len(nums)+1):
            if i not in a: L1.append(i)
        return L1