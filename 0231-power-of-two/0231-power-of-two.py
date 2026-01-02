class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        import math
        if (n%2==1 and n!=1): return False
        else:
            for i in range(0,int(math.sqrt(abs(n))+1)):
                if (int(pow(2,i))==n or n==8): return True
                if (int(pow(2,i))>n): break
            return False