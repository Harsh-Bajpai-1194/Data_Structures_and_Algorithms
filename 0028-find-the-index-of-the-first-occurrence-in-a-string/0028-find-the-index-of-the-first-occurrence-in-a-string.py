class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack==needle: return 0
        if len(needle)>len(haystack): return -1
        if needle in haystack or len(needle)==1:
            for i in range(len(haystack)):
                if haystack[i]==needle: return i
            for i in range(len(haystack)-len(needle)+1):
                if haystack[i:i+len(needle)]==needle: return i
        return -1