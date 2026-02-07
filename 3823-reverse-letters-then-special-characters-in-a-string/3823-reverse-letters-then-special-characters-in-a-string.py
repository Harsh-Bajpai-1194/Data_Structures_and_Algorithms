class Solution(object):
    def reverseByType(self, s):
        """
        :type s: str
        :rtype: str
        """
        a,b=[],[]
        for i in range(len(s)):
            if s[i].isalpha():
                a.append(s[i])
            else:
                b.append(s[i])
        a.reverse()
        b.reverse()
        s1=""
        for i in range(len(s)):
            if s[i].isalpha():
                s1+=a[0]
                a.pop(0)
            else:
                s1+=b[0]
                b.pop(0)
        return s1