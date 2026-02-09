class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) 
    {
        vector<int> px(n+1), xp(n+1);
        for(vector<int>& t:trust)
        {
            px[t[0]]++;
            xp[t[1]]++;
        }
        for (int i=1; i<=n; i++)
        {
            if (px[i]==0 && xp[i]==n-1) return i;
        }
        return -1;
    }
};