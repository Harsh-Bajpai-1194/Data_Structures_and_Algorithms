class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<vector<int>> result;
        vector<int> path;
        dfs(graph, 0, path, result);
        return result;
    }
private:
    void dfs(vector<vector<int>>& graph, int u, vector<int>& path, vector<vector<int>>& result) {
        path.push_back(u);
        if (u == graph.size() - 1) {
            result.push_back(path);
        } else {
            for (int nextNode : graph[u]) {
                dfs(graph, nextNode, path, result);
            }
        }
        path.pop_back();
    }
};