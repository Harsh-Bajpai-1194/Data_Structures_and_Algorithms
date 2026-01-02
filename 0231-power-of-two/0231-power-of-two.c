bool isPowerOfTwo(long long int n) 
{
    if (n%2==1 && n!=1) return false;
    else
    {
        for(int i=0;i<=sqrt(n);i++)
        {
            if ((int)pow(2,i)==n || n==8) return true;
            if ((int)pow(2,i)>n) break;
        }
        return false;
    }
}