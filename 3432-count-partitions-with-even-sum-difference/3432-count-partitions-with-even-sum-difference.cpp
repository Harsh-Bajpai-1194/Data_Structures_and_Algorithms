class Solution {
public:
    int countPartitions(vector<int>& nums) {
        int c=0,i=0,total=0,right_sum;
        while (i<nums.size()) total+=nums[i++];
        for (int i=1; i<nums.size(); i++)
        {
            int left_sum=0,j=0;
            while (j<i) left_sum+=nums[j++];
            right_sum=total-left_sum;
            if (left_sum%2==right_sum%2) c+=1;
        }
        return c;
    }
};