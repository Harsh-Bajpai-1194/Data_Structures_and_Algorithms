class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        for (int i=1; i<=n; i++)
        {
            int px=0, xp=0;
            for(vector<int>& t:trust)
            {
                if (t[0]==i) px++;
                else if (t[1]==i) xp++;
            }
            if (px==0 && xp==n-1) return i;
        }
        return -1;
    }
};