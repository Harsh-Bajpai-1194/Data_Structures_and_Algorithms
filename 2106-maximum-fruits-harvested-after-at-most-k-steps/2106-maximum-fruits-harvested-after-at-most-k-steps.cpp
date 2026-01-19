class Solution {
public:
    int maxTotalFruits(vector<vector<int>>& fruits, int startPos, int k) {
        int ans = 0;

        int maxRight = max(startPos, fruits.back()[0]);
        vector<int> amounts(maxRight + 1, 0);

        for (const auto& fruit : fruits) {
            int position = fruit[0];
            int amount = fruit[1];
            amounts[position] = amount;
        }

        vector<int> prefix(maxRight + 2, 0);
        for (int i = 0; i <= maxRight; ++i) {
            prefix[i + 1] = prefix[i] + amounts[i];
        }

                auto getFruits = [&](int leftSteps, int rightSteps) -> int {
            int l = max(0, startPos - leftSteps);
            int r = min(maxRight, startPos + rightSteps);
            return prefix[r + 1] - prefix[l];
        };

            for (int rightSteps = 0; rightSteps <= min(maxRight - startPos, k); ++rightSteps) {
            int leftSteps = max(0, k - 2 * rightSteps); 
            ans = max(ans, getFruits(leftSteps, rightSteps));
        }

            for (int leftSteps = 0; leftSteps <= min(startPos, k); ++leftSteps) {
            int rightSteps = max(0, k - 2 * leftSteps); 
            ans = max(ans, getFruits(leftSteps, rightSteps));
        }

        return ans;
    
    }
};