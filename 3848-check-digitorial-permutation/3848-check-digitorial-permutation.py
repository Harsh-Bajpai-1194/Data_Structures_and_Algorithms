class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        L=[1,1,2,6,24,120,720,720*7,720*7*8,720*7*8*9]
        num=n
        sum=0
        while(n!=0):
            digit=n%10
            n//=10
            sum+=L[digit]
        return (sorted(str(sum))==sorted(str(num)))