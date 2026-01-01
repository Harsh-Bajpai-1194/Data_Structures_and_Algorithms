class Solution {
    public boolean isPalindrome(int x) {
        int sum=0,num=x;
        while(num!=0)
        {
            sum=sum*10+num%10;
            num/=10;
        }
        if (x<0) return false;
        else if (sum==x) return true;
        else return false;
    }
}