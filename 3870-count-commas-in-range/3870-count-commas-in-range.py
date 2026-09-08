class Solution:
    def countCommas(self, n: int) -> int:
        c=0; max=1000; d=1
        while n>=max:
            c+=(min((max*1000)-1,n)-max+1)*d
            max*=1000
            d+=1
        return c