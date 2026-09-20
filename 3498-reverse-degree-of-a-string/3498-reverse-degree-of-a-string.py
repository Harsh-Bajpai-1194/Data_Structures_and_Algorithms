class Solution:
    def reverseDegree(self, s: str) -> int:
        s1="[abcdefghijklmnopqrstuvwxyz"
        sum=0
        for i in range(len(s)):
            sum+=(27-s1.index(s[i]))*(i+1)
        return sum