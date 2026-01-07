class Solution {
public:
    int longestSubarray(vector<int>& nums)
    {
        int i=0; int count=0; int a=0;
        for(int j=0;j<nums.size();j++)
        {
            if (nums[j]==0) count+=1;
            while (count>1)
            {
                if (nums[i]==0) count-=1;
                i+=1;
            }
            a=max(a,(j-i));
        }   
        return a;
    }
};