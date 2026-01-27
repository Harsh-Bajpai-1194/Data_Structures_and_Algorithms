class Solution {
public:
    int trap(vector<int>& height) {
        int n=height.size();
        if (n==0) return 0;
        vector<int> Prefix_Max(n);
        vector<int> Suffix_Max(n);
        Prefix_Max[0]=height[0];
        for (int i=1; i<n; i++) 
        {
            Prefix_Max[i]=max(Prefix_Max[i-1], height[i]);
        }
        Suffix_Max[n-1]=height[n-1];
        for (int i=n-2; i>=0; i--) 
        {
            Suffix_Max[i]=max(Suffix_Max[i+1], height[i]);
        }
        int ans=0;
        for (int i=0; i<n; i++) 
        {
            ans+=min(Prefix_Max[i],Suffix_Max[i])-height[i];
        }
        return ans;
    }
};