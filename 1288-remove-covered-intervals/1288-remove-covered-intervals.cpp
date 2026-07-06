class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b) 
        {
            if (a[0] == b[0]) return (a[1]>b[1]);
            return (a[0]<b[0]);
        });
        int count = 0, maxEnd = 0;
        for (auto& i : intervals) 
        {
            if (i[1] > maxEnd) 
            {
                count++;
                maxEnd = i[1];
            }
        }
        return count;
    }
};