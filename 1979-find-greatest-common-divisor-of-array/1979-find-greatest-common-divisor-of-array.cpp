class Solution {
public:
    int findGCD(vector<int>& nums) {
        int min=nums[0], max=nums[0];
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]<min) min=nums[i];
            else if (nums[i]>max) max=nums[i];
        }
        int num1=min,num2=max;
        while(num1>0)
        {
            int temp=num2%num1;
            num2=num1;
            num1=temp;
        }
        return num2;
    }
};