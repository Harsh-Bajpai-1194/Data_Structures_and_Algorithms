class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=0
        for i in nums:
            sum=0
            count=0
            for j in range(1,int(i**0.5)+1):
                if i<6: break
                if i%j==0:
                    if (j!=(i//j)):
                        sum+=j+(i//j)
                        count+=2
                    else:
                        sum+=j
                        count+=1
            if count==4: total+=sum
        return total