/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortedSquares(int* nums, int numsSize, int* returnSize) {
    int* L=(int*)malloc(numsSize * sizeof(int));
    *returnSize=numsSize;
    int l=0,r=numsSize-1,index=numsSize-1;
    while (l<=r) 
    {
        int lVal=nums[l]*nums[l];
        int rVal=nums[r]*nums[r];
        if (lVal>rVal) 
        {
            L[index] = lVal;
            l++;
        } 
        else 
        {
            L[index] = rVal;
            r--;
        }
        index--;
    }
    return L;
}