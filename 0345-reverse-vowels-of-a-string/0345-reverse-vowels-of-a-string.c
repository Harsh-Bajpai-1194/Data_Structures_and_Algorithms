int isVowel(char c) 
{
    c=tolower(c);
    return c=='a' || c=='e' || c=='i' || c=='o' || c=='u';
}
char* reverseVowels(char* s) {
    int left=0,right=strlen(s)-1;
    while (left < right) 
    {
        if (!isVowel(s[left])) left++;
        else if (!isVowel(s[right])) right--;
        else
        {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
    }
    return s;
}