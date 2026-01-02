void moveZeroes(int* nums, int numsSize) {
    int zi=0;
    for(int i=0;i<numsSize;i++)
    {
        if (nums[i]!=0)
        {
            nums[zi]=nums[i];
            zi++;
        }
    }
    while (zi<numsSize)
    {
        nums[zi]=0;
        zi++;
    }
}