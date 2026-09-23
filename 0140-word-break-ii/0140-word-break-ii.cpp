// Backtracking
class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        vector<string> all;
        string par; // partial
        int i = 0;
        dfs(s, dict, i, par, all);
        return all;
    }
private:
    void dfs(string& s, unordered_set<string>& dict, int i, string par, vector<string>& all) {
        if(i == s.size()) all.push_back(par);
        else {
            for(int j = i; j < s.size(); j++) {
                string word = s.substr(i, j-i+1);
                if(dict.find(word) != dict.end()) {
                    string par2 = par;
                    if(!par2.empty()) par2 += " ";
                    par2 += word;
                    dfs(s, dict, j+1, par2, all);
                }
            }
        }
    }
};