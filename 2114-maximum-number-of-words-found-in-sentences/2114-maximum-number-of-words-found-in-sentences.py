class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max=0
        for i in sentences:
            count=1
            for j in i:
                if j==" ":
                    count+=1
            if count>max:
                max=count
        return max