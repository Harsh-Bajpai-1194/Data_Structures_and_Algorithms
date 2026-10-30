class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<vector<int>> F1(1 + amount, vector<int>(1 + coins.size()));
        for (int t = 0; t <= amount; t++) {
            for (int i = coins.size(); i >= 0; i--) {
                if (t == 0)
                    F1[t][i] = 0;
                else if (i == coins.size())
                    F1[t][i] = -1;
                else {
                    F1[t][i] = F1[t][i + 1];
                    if (coins[i] <= t) {
                        int sub = F1[t - coins[i]][i];
                        if (sub != -1 && (F1[t][i] == -1 || 1 + sub < F1[t][i])) {
                            F1[t][i] = 1 + sub;
                        }
                    }
                }
            }
        }
        return F1[amount][0];
    }
};