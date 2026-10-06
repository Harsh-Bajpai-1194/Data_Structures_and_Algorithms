int minAddToMakeValid(char* s) {
    int c = 0, c1 = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '(') c+=1;
        else
        {
            if (c>0) c-=1;
            else c1+=1;
        }
    }
    return c + c1;
}