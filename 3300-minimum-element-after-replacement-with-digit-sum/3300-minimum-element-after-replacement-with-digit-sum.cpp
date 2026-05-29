class Solution {
public:
    int minElement(vector<int>& nums) {
        for(int i=0; i<nums.size(); i++)
        {   
            int a = nums[i];
            int sum = 0;
            while (a!=0)
            {
                sum = sum + (a % 10);
                a = a / 10;
            }
            nums[i]=sum;
        }
        int min=nums[0];
        for (int i=0; i<nums.size(); i++)
        {
            if (nums[i]<min) min=nums[i];
        }
        return min;
    }
};