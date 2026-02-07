class Solution(object):
    def countMonobit(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        for i in range(n+1):
            a=bin(i)[2:]
            if len(list(set(list(a))))==1:
                c+=1
        return c