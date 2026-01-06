class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square=[x*x for x in nums]
        square.sort()
        return square