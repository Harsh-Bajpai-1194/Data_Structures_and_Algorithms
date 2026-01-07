class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        L=[]
        for i in range(len(nums)//2):
            L.append(nums[i])
            L.append(nums[i+len(nums)//2])
        return L