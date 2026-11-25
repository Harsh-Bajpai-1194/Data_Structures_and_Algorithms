// Naive implementation O(2^n) time
class Solution1 {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        return f1(questions, 0);
    }

private:
    long long f1(vector<vector<int>>& questions, int i) {
        if (i >= questions.size()) return 0;
        long long skip = f1(questions, i + 1);
        long long solve = questions[i][0] + f1(questions, i + 1 + questions[i][1]);
        return max(skip, solve);
    }
};

// Iterative DP (aka Memoization)
// 0(n) time. 0(n) extra space, 0(n) stack space
class Solution {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        vector<long long> F1(questions.size() + 1, -1);
        return f1(questions, 0, F1);
    }
private:
    long long f1(vector<vector<int>>& questions, int i, vector<long long>& F1) {
        if (i >= (int)questions.size()) return 0;
        if (F1[i] != -1) return F1[i];
        long long skip = f1(questions, i + 1, F1);
        long long solve = questions[i][0] + f1(questions, i + 1 + questions[i][1], F1);
        return F1[i] = max(skip, solve);
    }
};