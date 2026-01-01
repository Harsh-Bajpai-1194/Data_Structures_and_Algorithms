class Solution {
public:
    int maxArea(vector<int>& height) {
        int max=0,i=0,j=height.size()-1,a;
        while(i<j)
        {
            if (height[i]<height[j]) a=height[i]*(j-i);
            else a=height[j]*(j-i);
            if (a>max) max=a;
            if (height[i]<height[j]) i=i+1;
            else j=j-1;
        }
        return max;
    }
};