class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts=Counter(nums)  
        max_length = 0  
        for num, count in counts.items():  
            if num + 1 in counts:  
                max_length = max(max_length, count + counts[num + 1])  
        return max_length