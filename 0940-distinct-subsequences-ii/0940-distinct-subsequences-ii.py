class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD=10**9+7
        total=0
        dp=[0]*26
        for i in s:
            i=ord(i)-97
            new=total+1-dp[i]
            total=(total+new)%MOD
            dp[i]=(dp[i]+new)%MOD
        return total