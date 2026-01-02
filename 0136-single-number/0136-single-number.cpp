class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int count=0;
        for(int i=0; i<nums.size(); i++)
        {
            int a=nums[i];
            for(int j=0; j<nums.size(); j++)
            {
                if (nums[j]==a) count+=1;
            }
            if (count==1) return a;
            count=0;
        }
        return 0;
    }
};