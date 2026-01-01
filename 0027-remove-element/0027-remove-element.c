int removeElement(int* nums, int numsSize, int val) {
    int i=0,temp;
    int j=numsSize-1;
    while(i<=j)
    {
        if (nums[i]==val)
        {
            temp=nums[i];
            nums[i]=nums[j];
            nums[j]=temp;
            j=j-1;
        }
        else i=i+1;
    }
    return i;
}