class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(image)):
            image[i]=image[i][-1::-1]
            for j in range(len(image)): image[i][j]=(image[i][j]+1)%2
        return image