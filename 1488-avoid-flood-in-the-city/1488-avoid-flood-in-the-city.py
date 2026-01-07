class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        from bisect import bisect_right, insort
        r=rains
        d, f, l, a = [], set(), {}, [-1]*len(r)
        for i,x in enumerate(r):
            if x:
                if x in f:
                    j=bisect_right(d,l[x])
                    if j==len(d):return[]
                    a[d.pop(j)]=x
                f.add(x);l[x]=i
            else: insort(d,i);a[i]=1
        return a