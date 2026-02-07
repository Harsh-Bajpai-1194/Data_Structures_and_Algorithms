int maxFreqSum(char* s) {
    int max_vow=0,max_con=0;
    for(int i=0;i<strlen(s);i++)
    {
        if (s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u')
        {
            int count1=0;
            for(int j=0;j<strlen(s);j++)
            {
                if (s[j]==s[i]) count1+=1;
            }
            if (count1>max_vow) max_vow=count1;
        } 
        else
        {
            int count2=0;
            for(int k=0;k<strlen(s);k++)
            {
                if (s[k]==s[i]) count2+=1;
            }
            if (count2>max_con) max_con=count2;
        }
    }
    return max_vow+max_con;
}