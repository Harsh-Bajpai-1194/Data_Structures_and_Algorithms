class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0  
        streak = 0  
        for num in nums:
            if num == 0:
                streak += 1
                count += streak
            else:
                streak = 0
        return count