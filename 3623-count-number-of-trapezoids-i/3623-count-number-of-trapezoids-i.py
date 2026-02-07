class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cnt={}
        for i,y in points: cnt[y]=cnt.get(y,0)+1
        arr=[]
        for v in cnt.values():
            if v>1: arr.append(v*(v-1)//2)
        total=sum(arr)
        sq=sum(x*x for x in arr)
        return ((total*total-sq)//2)%(10**9+7)