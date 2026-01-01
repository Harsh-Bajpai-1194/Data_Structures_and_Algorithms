class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend==0: return 0
        elif divisor==1: return dividend
        elif dividend==divisor: return 1
        elif dividend<0 and divisor==-1: return -dividend-1
        elif dividend<0 and divisor>0: return (-1)*((-dividend)/divisor)
        elif dividend<0 and divisor<0 or dividend>0 and divisor>0: return dividend/divisor
        elif dividend>0 and divisor<0: return -(dividend/-divisor)