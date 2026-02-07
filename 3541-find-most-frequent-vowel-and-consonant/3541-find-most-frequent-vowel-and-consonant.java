class Solution {
    public int maxFreqSum(String s) {
        int max_vow=0,max_con=0;
        for(int i=0;i<s.length();i++)
        {
            char ch=s.charAt(i);
            if (ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u')
            {
                int count1=0;
                for(int j=0;j<s.length();j++)
                {
                    char ch1=s.charAt(j);
                    if (ch1==ch) count1+=1;
                }
                if (count1>max_vow) max_vow=count1;
            } 
            else
            {
                int count2=0;
                for(int k=0;k<s.length();k++)
                {
                    char ch2=s.charAt(k);
                    if (ch2==ch) count2+=1;
                }
                if (count2>max_con) max_con=count2;
            }
        }
        return max_vow+max_con;
    }
}