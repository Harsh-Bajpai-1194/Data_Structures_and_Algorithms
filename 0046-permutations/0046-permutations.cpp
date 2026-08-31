class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        int n = nums.size();
        vector<int> perm;
        vector<bool> available(n, true);
        vector<vector<int>> all;
        dfs(nums, available, perm, all);
        return all;
    }
private:
    void dfs(vector<int>& nums, vector<bool>& available, vector<int>& perm, vector<vector<int>>& all) {
        if(perm.size() == nums.size()) {
            all.push_back(perm);
        } else {
            for(int i = 0; i < nums.size(); i++) {
                if(available[i]) {
                    perm.push_back(nums[i]);
                    available[i] = false;
                    dfs(nums, available, perm, all);
                    available[i] = true;
                    perm.pop_back();
                }
            }
        }
    }
};