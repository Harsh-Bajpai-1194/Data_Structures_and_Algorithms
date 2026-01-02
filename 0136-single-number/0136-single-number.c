int singleNumber(int* nums, int numsSize) {
    int count=0;
    for(int i=0; i<numsSize; i++)
    {
        int a=nums[i];
        for(int j=0; j<numsSize; j++)
        {
            if (nums[j]==a) count+=1;
        }
        if (count==1) return a;
        count=0;
    }
    return 0;
}