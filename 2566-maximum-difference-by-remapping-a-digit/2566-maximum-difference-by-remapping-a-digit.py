class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        for d in num_str:
            if d != '9':
                max_str = num_str.replace(d, '9')
                break
        else:
            max_str = num_str
        for d in num_str:
            if d != '0':
                min_str = num_str.replace(d, '0')
                break
        else:
            min_str = num_str
        return int(max_str) - int(min_str)