#define MOD 1000000007LL
typedef long long ll;
int colorTheGrid(int m, int n) {
    int pat[60], patCnt = 0, pow3 = 1;
    for (int i = 0; i < m; ++i) pow3 *= 3;
    for (int x = 0; x < pow3; ++x) {
        int ok = 1, y = x, prev = -1;
        for (int r = 0; r < m && ok; ++r) {
            int c = y % 3;
            if (c == prev) ok = 0;
            prev = c;
            y /= 3;
        }
        if (ok) pat[patCnt++] = x;
    }
    char good[60][60] = {0};
    for (int i = 0; i < patCnt; ++i)
        for (int j = 0; j < patCnt; ++j) {
            int a = pat[i], b = pat[j], ok = 1;
            for (int r = 0; r < m && ok; ++r) {
                if (a % 3 == b % 3) ok = 0;
                a /= 3; b /= 3;
            }
            good[i][j] = ok;
        }
    ll dp[60] = {0}, nxt[60] = {0};
    for (int i = 0; i < patCnt; ++i) dp[i] = 1;
    for (int col = 1; col < n; ++col) {
        for (int j = 0; j < patCnt; ++j) nxt[j] = 0;
        for (int p1 = 0; p1 < patCnt; ++p1)
            for (int p2 = 0; p2 < patCnt; ++p2)
                if (good[p1][p2])
                    nxt[p2] = (nxt[p2] + dp[p1]) % MOD;
        for (int j = 0; j < patCnt; ++j) dp[j] = nxt[j];
    }
    ll ans = 0;
    for (int i = 0; i < patCnt; ++i) ans = (ans + dp[i]) % MOD;
    return (int)ans;
}