class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        from collections import Counter
        num=n+1
        while True:
            count=Counter(str(num))
            if all(int(i)==j for i,j in count.items()): return num
            num+=1