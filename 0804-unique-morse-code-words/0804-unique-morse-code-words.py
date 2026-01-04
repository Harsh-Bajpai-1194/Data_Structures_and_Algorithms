class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        a=list("abcdefghijklmnopqrstuvwxyz")
        code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        L=[]
        for i in range(len(words)):
            s=""
            for j in range(len(words[i])):
                s+=code[a.index(words[i][j])]
            L.append(s)
        return len(set(L))