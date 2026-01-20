class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        word = "a"  
        while len(word) < k:  
            new_word = ""  
            for char in word:  
                new_word += chr(((ord(char) - ord('a')) + 1) % 26 + ord('a'))  
            word += new_word  
        return word[k-1]