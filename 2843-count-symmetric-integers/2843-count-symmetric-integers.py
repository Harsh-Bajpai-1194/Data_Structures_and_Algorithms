class Solution(object):
    def countSymmetricIntegers(self, low, high):
        count=0
        for i in range(low,high+1):
            if len(str(i))%2==0:
                half=len(str(i))//2
                left_sum = sum(int(d) for d in str(i)[:half])
                right_sum = sum(int(d) for d in str(i)[half:])
                if (left_sum==right_sum):
                    count+=1
        return count