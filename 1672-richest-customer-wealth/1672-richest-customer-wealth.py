class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max=0
        for i in accounts:
            sum=0
            for j in i:
                sum+=j
            if sum>max:
                max=sum
        return max