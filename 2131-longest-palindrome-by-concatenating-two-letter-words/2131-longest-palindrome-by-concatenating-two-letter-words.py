class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = Counter(words)
        result = 0
        used_center = False
        for word in count:
            rev = word[::-1]
            if word != rev:
                if rev in count:
                    pair = min(count[word], count[rev])
                    result += pair*4
                    count[word] -= pair
                    count[rev] -= pair
            else:
                pair = count[word] // 2
                result += pair * 4
                count[word] -= pair * 2
        for word in count:
            if word[0] == word[1] and count[word] > 0 and not used_center:
                result += 2 
                used_center = True
                break
        return result