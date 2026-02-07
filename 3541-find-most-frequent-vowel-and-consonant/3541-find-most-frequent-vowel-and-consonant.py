class Solution:
    def maxFreqSum(self, s: str) -> int:
        max_vow,max_con=0,0
        for i in s:
            if i in "aeiou" and s.count(i)>max_vow: max_vow=s.count(i)
            elif i not in "aeiou" and s.count(i)>max_con: max_con=s.count(i)
        return max_vow+max_con