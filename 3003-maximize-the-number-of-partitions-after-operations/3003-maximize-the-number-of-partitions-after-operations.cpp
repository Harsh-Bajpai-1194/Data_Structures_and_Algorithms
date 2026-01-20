class Solution {
public:
    int maxPartitionsAfterOperations(string s, int k) {
        unordered_map<long, int> memo;
        return helper(s, 0, true, 0, k, memo) + 1;
    }

private:
    int helper(const string& s, int i, bool canChange, int mask, int k,
               unordered_map<long, int>& memo) {
        if (i == s.size())
            return 0;

        long key = ((long)i << 27) | ((canChange ? 1L : 0L) << 26) | mask;
        if (memo.count(key))
            return memo[key];

        int res = compute(s, i, canChange, mask, 1 << (s[i] - 'a'), k, memo);

        if (canChange) {
            for (int j = 0; j < 26; ++j)
                res = max(res, compute(s, i, false, mask, 1 << j, k, memo));
        }

        return memo[key] = res;
    }

    int compute(const string& s, int i, bool nextCanChange, unsigned mask,
                int newBit, int k, unordered_map<long, int>& memo) {
        unsigned newMask = mask | newBit;
        if (__builtin_popcount(newMask) > k)
            return 1 + helper(s, i + 1, nextCanChange, newBit, k, memo);
        return helper(s, i + 1, nextCanChange, newMask, k, memo);
    }
};