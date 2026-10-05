// S4: Tail recursion optimization the Greedy reccurrence
// O(n) time, O(1) extra space
class Solution {
    int n, k;
public:
    bool isSubsequence(string pattern, string text) {
        n = text.size();
        k = pattern.size();
        int i = 0, j = 0;
        
        while (i != n) {
            if (j < k && text[i] == pattern[j]) {
                i++;
                j++;
            } else {
                i++;
            }
        }
        
        return (j == k);
    }
};

// S3: Greedy reccurrence
// 0(2^n) time, 0(1) extra space, 0(n) stack space
/*
class Solution {
    int n, k;
public:
    bool isSubsequence(string s, string t) {
        n = t.size();
        k = s.size();
        return f1(t, 0, s, 0);
    }
private:
    bool f1(string& text, int i, string& pattern, int j) {
        if (j == k) return true;
        if (i == n) return false;

        if (text[i] == pattern[j]) {
            return f1(text, i + 1, pattern, j + 1);
        } else {
            return f1(text, i + 1, pattern, j);
        }
    }
};
*/