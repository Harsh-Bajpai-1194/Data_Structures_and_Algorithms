class Solution(object):
    def bestTower(self, towers, center, radius):
        """
        :type towers: List[List[int]]
        :type center: List[int]
        :type radius: int
        :rtype: List[int]
        """
        a,L=-1,[-1]*2
        b,c=center
        for i,j,k in towers:
            distance=abs(abs(i-b)+abs(j-c))
            if (distance<=radius and a<k): a,L=k,[i,j]
            elif (distance<=radius and a==k):
                if ((i<L[0]) or (L[0]==i and j<L[1])): L=[i,j]
        return L