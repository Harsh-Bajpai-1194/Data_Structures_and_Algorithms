int longestSubarray(int* nums, int numsSize) {
    int i=0; int count=0; int a=0;
    for(int j=0;j<numsSize;j++)
    {
        if (nums[j]==0) count+=1;
        while (count>1)
        {
            if (nums[i]==0) count-=1;
            i+=1;
        }
        a=(a>=(j-i))?a:(j-i);
    }   
    return a;
}