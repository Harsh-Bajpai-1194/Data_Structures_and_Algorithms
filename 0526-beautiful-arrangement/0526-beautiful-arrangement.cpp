class Solution {
public:
    int countArrangement(int n) {
        int count = 0;
        vector<bool> visited(n + 1, false);
        dfs(n, 1, visited, count);
        return count;
    }

private:
    void dfs(int n, int pos, vector<bool>& visited, int& count) {
        if (pos > n) {
            count++;
            return;
        }
        for (int i = 1; i <= n; i++) {
            if (!visited[i] && (i % pos == 0 || pos % i == 0)) {
                visited[i] = true;
                dfs(n, pos + 1, visited, count);
                visited[i] = false;
            }
        }
    }
};