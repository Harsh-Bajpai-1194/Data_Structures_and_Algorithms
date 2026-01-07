class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        for i in range(n):
            nums.append(start+2*i)
        for i in range(1,n):
            nums[i]=nums[i-1]^nums[i]
        return nums[n-1]