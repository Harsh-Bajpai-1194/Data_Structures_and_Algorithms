//Note: The returned array must be malloced, assume caller calls free()
void merge(int* nums,int l,int mid,int r)
{   int n1=mid-l+1, n2=r-mid;
    int*L=malloc(n1*sizeof(int)); int*R=malloc(n2*sizeof(int));
    for(int i=0; i<n1; i++) L[i]=nums[l+i];
    for(int j=0; j<n2; j++) R[j]=nums[mid+1+j];
    int i=0,j=0,k=l;
    while(i<n1 && j<n2) nums[k++]= (L[i]<=R[j]) ? L[i++] : R[j++];
    while(i<n1) nums[k++]=L[i++];
    while(j<n2) nums[k++]=R[j++];
    free(L); free(R);
}
void merge_sort(int* nums,int l,int r)
{   if(l<r) { merge_sort(nums,l,l+(r-l)/2); merge_sort(nums,l+(r-l)/2+1,r); 
    merge(nums,l,l+(r-l)/2,r); }
}
int* sortArray(int* nums,int numsSize,int* returnSize){
    merge_sort(nums,0,numsSize-1);
    *returnSize=numsSize; return nums; 
}