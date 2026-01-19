long long kthSmallestProduct(int* nums1, int nums1Size, int* nums2, int nums2Size, long long k) {  
    long long low = -1e10, high = 1e10, ans = 0;

    while (low <= high) {  
        long long mid = low + (high - low) / 2;  
        long long count = 0;

        for (int i = 0; i < nums1Size; i++) {  
            if (nums1[i] >= 0) {  
                int left = 0, right = nums2Size - 1;  
                while (left <= right) {  
                    int m = left + (right - left) / 2;  
                    if ((long long)nums1[i] * nums2[m] <= mid)  
                        left = m + 1;  
                    else  
                        right = m - 1;  
                }  
                count += left;  
            } else {  
                int left = 0, right = nums2Size - 1;  
                while (left <= right) {  
                    int m = left + (right - left) / 2;  
                    if ((long long)nums1[i] * nums2[m] <= mid)  
                        right = m - 1;  
                    else  
                        left = m + 1;  
                }  
                count += (nums2Size - left);  
            }  
        }

        if (count < k)  
            low = mid + 1;  
        else {  
            ans = mid;  
            high = mid - 1;  
        }  
    }

    return ans;  
}  