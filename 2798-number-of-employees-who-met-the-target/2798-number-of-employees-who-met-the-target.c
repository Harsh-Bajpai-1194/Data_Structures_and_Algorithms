int numberOfEmployeesWhoMetTarget(int* hours, int hoursSize, int target) 
{
    long long int count=0;
    for(int i=0;i<hoursSize;i++)
    {
        if (hours[i]>=target)
        {
             count=count+1;
        }
    }
    return count;
}