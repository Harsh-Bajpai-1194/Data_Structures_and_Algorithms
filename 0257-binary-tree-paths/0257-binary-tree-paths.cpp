/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<vector<int>> paths = f1(root);
        vector<string> output;
        for(vector<int>& path : paths) 
        {
            string p = to_string(path[0]);
            for (int i = 1; i < path.size(); i++) 
            {
                p += "->" + to_string(path[i]);
            }
            output.push_back(p);
        }
        return output;
    }
private:
    vector<vector<int>> f1(TreeNode* root) {
    if (!root) return {};
    vector<vector<int>> paths;
    TreeNode* node = root;
    vector<int> path = {root->val};
    map<TreeNode*, vector<int>> pending;
    while(node != nullptr || !pending.empty()) 
    {
        while(node != nullptr) 
        {
            if(node->left == nullptr && node->right == nullptr) 
            {
                paths.push_back(path);
            }
            if(node->right) 
            {
                pending[node->right] = path;
                pending[node->right].push_back(node->right->val);
            }
            node = node->left;
            if(node) 
            {
            path.push_back(node->val);
            }
        }
        if(pending.empty()) break;
        auto it = prev(pending.end());
        node = it->first;
        path = it->second;
        pending.erase(it);
    }
    return paths;
}
};