class Solution:
    def product(self, i):
        prod = 1
        while (i != 0):
            prod = prod * (i % 10)
            i = i // 10
        return prod
    def smallestNumber(self, n, t):
        for i in range(n, n+t):
            if self.product(i) % t == 0: 
                return i

class Solution1:
    def smallestNumber(self, n, t):
        for i in range(n, n+t):
            prod = 1
            for j in range(len(str(i))):
                prod = prod * int(str(i)[j])
            if prod % t == 0: 
                return i

class Solution2:
    def smallestNumber(self, n, t):
        for i in range(n, 1000):
            prod = 1
            for j in range(len(str(i))):
                prod = prod * int(str(i)[j])
            if prod % t == 0: 
                return i