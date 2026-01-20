int differenceOfSums(int n, int m) {
    int total_sum = n*(n+1)/2;
    int divisible_sum=0;
    for(int i=m;i<n+1;i=i+m)
    {
        divisible_sum=divisible_sum+i;
    }  
    return total_sum-2*divisible_sum;
}