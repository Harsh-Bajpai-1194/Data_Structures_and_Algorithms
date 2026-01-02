class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        for i in s:
            if i.isalpha() or i.isdigit():
                a+=i
        if a.lower()==a.lower()[::-1]:
            return True
        return False