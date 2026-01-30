int trap(int* height, int heightSize) {
    int ans=0,lmax=0,rmax=0,l=0,r=heightSize-1;
    while (l<r)
    {
        if (height[l]<=height[r])
        {
            if (lmax>height[l]) ans+=lmax-height[l];
            else lmax=height[l];
            l++;
        }
        else
        {
            if (rmax>height[r]) ans+=rmax-height[r];
            else rmax=height[r];
            r--;
        }
    }
    return ans;
}