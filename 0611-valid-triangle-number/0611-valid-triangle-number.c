#include <stdio.h>
#include <stdlib.h>
void merge(int* nums, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    int* L = (int*)malloc(n1 * sizeof(int));
    int* R = (int*)malloc(n2 * sizeof(int));
    for (int i = 0; i < n1; i++)
        L[i] = nums[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = nums[mid + 1 + j];
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) nums[k++] = L[i++];
        else nums[k++] = R[j++];
    }    
    while (i < n1) nums[k++] = L[i++];
    while (j < n2) nums[k++] = R[j++];
    free(L);
    free(R);
}
void mergeSort(int* nums, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(nums, left, mid);
        mergeSort(nums, mid + 1, right);
        merge(nums, left, mid, right);
    }
}
int triangleNumber(int* nums, int numsSize) {
    mergeSort(nums, 0, numsSize - 1);
    int count = 0;
    for (int i = numsSize - 1; i >= 2; i--) {
        int l = 0, r = i - 1;
        while (l < r) {
            if (nums[l] + nums[r] > nums[i]) {
                count += (r - l);
                r--;
            } 
            else {
                l++;
            }
        }
    }
    return count;
}