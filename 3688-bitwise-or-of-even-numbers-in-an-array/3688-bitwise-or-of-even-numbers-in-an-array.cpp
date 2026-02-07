class Solution {
public:
    int evenNumberBitwiseORs(vector<int>& nums) {
        int sum=0;
        for(int i=0;i<nums.size();i++)
        {
            if (nums[i]%2==0) sum=sum|nums[i];
        }
        return sum;
    }
};