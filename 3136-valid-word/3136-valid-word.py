class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:  
            return False
        vowels = "aeiouAEIOU"  
        has_vowel = False  
        has_consonant = False
        for char in word:  
            if not ('0' <= char <= '9' or 'a' <= char <= 'z' or 'A' <= char <= 'Z'):  
                return False  
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':  
                if char in vowels:  
                    has_vowel = True  
                else:  
                    has_consonant = True
        return has_vowel and has_consonant