class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        A=nums
        n = len(A)
        if ~n&1: return True
        def maxDiff(i: int, j: int) -> int:
            if i==j: return A[i]
            return max(A[i] - maxDiff(i + 1, j),A[j] - maxDiff(i, j - 1))
        return maxDiff(0, n - 1) >= 0