class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=strs[[len(i) for i in strs].index(min([len(i) for i in strs]))]
        for i in range(len(a)):
            for j in range(len(strs)):
                if a[i]!=strs[j][i]: return a[:i]
        return a