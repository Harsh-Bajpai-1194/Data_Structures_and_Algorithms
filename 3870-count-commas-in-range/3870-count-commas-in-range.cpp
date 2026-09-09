class Solution {
public:
    long long countCommas(int n) {
        long long ans = 0;
        long long base = 1000;
        for (int i = 1; i < 6; i++) {
            ans += max((long long) 0, n - base + 1);
            base *= 1000;
        }
        return ans;
    }
};