class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10**9 + 7  
        pat = [0] * 60  
        pat_cnt = 0  
        pow3 = 1  
        for _ in range(m):  
            pow3 *= 3  
        for x in range(pow3):  
            ok = 1  
            y = x  
            prev = -1  
            for _ in range(m):  
                c = y % 3  
                if c == prev:  
                    ok = 0  
                prev = c  
                y //= 3  
            if ok:  
                pat[pat_cnt] = x  
                pat_cnt += 1  
        good = [[0] * 60 for _ in range(60)]  
        for i in range(pat_cnt):  
            for j in range(pat_cnt):  
                a, b, ok = pat[i], pat[j], 1  
                for _ in range(m):  
                    if a % 3 == b % 3:  
                        ok = 0  
                    a //= 3  
                    b //= 3  
                good[i][j] = ok  
        dp = [0] * 60  
        nxt = [0] * 60  
        for i in range(pat_cnt):  
            dp[i] = 1  
        for _ in range(1, n):  
            for j in range(pat_cnt):  
                nxt[j] = 0  
            for p1 in range(pat_cnt):  
                for p2 in range(pat_cnt):  
                    if good[p1][p2]:  
                        nxt[p2] = (nxt[p2] + dp[p1]) % mod  
            for j in range(pat_cnt):  
                dp[j] = nxt[j]  
        ans = 0  
        for i in range(pat_cnt):  
            ans = (ans + dp[i]) % mod  
        return ans