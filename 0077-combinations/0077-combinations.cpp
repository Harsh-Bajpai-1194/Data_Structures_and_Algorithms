// Backtracking
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> combinations;
        vector<int> partial;
        dfs(n, k, partial, combinations);
        return combinations;
    }
private:
    void dfs(int n, int k, vector<int>& partial, vector<vector<int>>& combinations) {
        if (k == 0) {
            vector<int> temp = partial;
            reverse(temp.begin(), temp.end());
            combinations.push_back(temp);
            return;
        }
        else // without n
        if (n >= k) {
            dfs(n - 1, k, partial, combinations);
            // with n
            partial.push_back(n);
            dfs(n - 1, k - 1, partial, combinations);
            partial.pop_back();
        }
    }
};