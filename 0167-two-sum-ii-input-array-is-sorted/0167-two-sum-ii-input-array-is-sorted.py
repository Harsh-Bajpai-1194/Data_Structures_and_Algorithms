class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        i=0
        j=n-1
        while i<j:
            if numbers[i]+numbers[j]==target:
                return [i+1,j+1]
            elif numbers[i]+numbers[j]<target:
                i+=1
            elif numbers[i]+numbers[j]>target:
                j-=1
        # this is optimised solution.
        
class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        for i in range(n-1):
            for j in range(i+1, n):
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]
        # brute force solution.