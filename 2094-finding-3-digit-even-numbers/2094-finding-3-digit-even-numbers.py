class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        from itertools import permutations
        res=set()
        for p in permutations(digits,3):
            if p[0]!=0 and p[2]%2==0:
                num=p[0]*100+p[1]*10+p[2]
                res.add(num)
        return sorted(res)