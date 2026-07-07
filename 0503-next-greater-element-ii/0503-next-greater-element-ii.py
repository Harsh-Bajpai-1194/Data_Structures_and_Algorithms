class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        stack=[]
        nums*=2
        Result=[-1]*2*n
        for i in range(2*n):
            if len(stack)==0:
                stack.append(i)
            while(len(stack)>0 and nums[i]>nums[stack[-1]]):
                Result[stack[-1]]=nums[i]
                stack.pop()
            stack.append(i)
        return Result[:n]