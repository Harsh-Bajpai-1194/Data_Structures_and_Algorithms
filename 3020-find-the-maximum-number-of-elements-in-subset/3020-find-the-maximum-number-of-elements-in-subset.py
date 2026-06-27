class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq=Counter(nums)
        res=(freq.pop(1,0)-1)|1
        for f in freq:
            x=f
            sq=sqrt(x)
            if sq**2==x and freq.get(sq, 0) > 1:
                continue
            n=0
            while x<=31622 and freq.get(x, 0) > 1:
                n,x=n+2,x**2
            res = max(res, n + ((x in freq) << 1) - 1)
        return res