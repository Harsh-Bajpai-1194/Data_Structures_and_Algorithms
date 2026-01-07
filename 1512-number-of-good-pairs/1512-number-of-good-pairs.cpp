class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int count=0;
        int numsSize=nums.size();
        for (int i=0; i<numsSize-1; i++)
        {
            for (int j=i+1; j<numsSize; j++)
            {
                if (nums[i]==nums[j]) count=count+1;
            }   
        }
        return count;  
        }
};