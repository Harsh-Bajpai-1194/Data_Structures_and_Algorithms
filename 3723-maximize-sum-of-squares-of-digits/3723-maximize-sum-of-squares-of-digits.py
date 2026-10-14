class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum>9*num:
            return ""
        q,r=divmod(sum,9)
        s = "9"*q
        if r>0:
            s += str(r)
        s+="0"*(num-len(s))
        return s