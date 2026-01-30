int trap(int* height, int heightSize) {
    int n = heightSize;
    if (n == 0) return 0;
    int Prefix_Max[n],Suffix_Max[n];
    Prefix_Max[0] = height[0];
    for (int i = 1; i < n; i++) 
    {
        if (height[i] > Prefix_Max[i-1]) Prefix_Max[i] = height[i];
        else Prefix_Max[i] = Prefix_Max[i-1];
    }
    Suffix_Max[n-1] = height[n-1];
    for (int i = n - 2; i >= 0; i--) 
    {
        if (height[i] > Suffix_Max[i+1]) Suffix_Max[i] = height[i];
        else Suffix_Max[i] = Suffix_Max[i+1];
    }
    int ans = 0;
    for (int i = 0; i < n; i++) {
        int min_height = (Prefix_Max[i] < Suffix_Max[i]) ? Prefix_Max[i] : Suffix_Max[i];
        ans += min_height - height[i];
    }
    return ans;
}