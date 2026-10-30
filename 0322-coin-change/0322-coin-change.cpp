class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<vector<int>> F1(2, vector<int>(1 + amount));
        for (int i = coins.size(); i >= 0; i--) {
            for (int t = 0; t <= amount; t++) {
                if (t == 0)
                    F1[i % 2][t] = 0;
                else if (i == coins.size())
                    F1[i % 2][t] = -1;
                else {
                    F1[i % 2][t] = F1[(i + 1) % 2][t];
                    if (coins[i] <= t) {
                        int sub = F1[i % 2][t - coins[i]];
                        if (sub != -1 && (F1[i % 2][t] == -1 || 1 + sub < F1[i % 2][t])) {
                            F1[i % 2][t] = 1 + sub;
                        }
                    }
                }
            }
        }
        return F1[0 % 2][amount];
    }
};