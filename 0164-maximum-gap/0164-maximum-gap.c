int compare_ints(const void *a, const void *b) 
{
    return (*(int*)a)-(*(int*)b);
}
int maximumGap(int* nums, int numsSize) 
{
    if (numsSize==1) return 0;
    qsort(nums, numsSize, sizeof(int), compare_ints);
    if (numsSize==2) return nums[1]-nums[0];
    int max=0;
    for (int i=1; i<numsSize-1; i++) {
        int gap=nums[i+1]-nums[i];
        if (gap>max) max=gap;
    }
    return max;
}