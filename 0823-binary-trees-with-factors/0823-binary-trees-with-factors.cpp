class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        unordered_map<int, long long> mp;
        long long MOD = 1e9 + 7;
        for (int x : arr) {
            mp[x] = 1;
        }
        
        for (int i = 0; i < arr.size(); i++) {
            for (int j = 0; j < i; j++) {
                if (arr[i] % arr[j] == 0) {
                    int right = arr[i] / arr[j];
                    if (mp.count(right)) {
                        long long combinations = (mp[arr[j]] * mp[right]) % MOD;
                        mp[arr[i]] = (mp[arr[i]] + combinations) % MOD;
                    }
                }
            }
        }
        long long ans = 0;
        for (auto& entry : mp) {
            ans = (ans + entry.second) % MOD;
        }
        return (int)ans;
    }
};