class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1: return 2**31 - 1
        if dividend == 0: return 0
        if divisor == 1: return dividend
        if dividend == divisor: return 1
        result=abs(dividend)//abs(divisor)
        if (dividend<0 and divisor>=0) or (dividend>=0 and divisor<0): result=-result
        return result