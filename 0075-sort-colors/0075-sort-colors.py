class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L=[]
        for i in nums:
            if i==0:
                L.append(i)
        for i in nums:
            if i==1:
                L.append(i)
        for i in nums:
            if i==2:
                L.append(i)
        nums[:]=L