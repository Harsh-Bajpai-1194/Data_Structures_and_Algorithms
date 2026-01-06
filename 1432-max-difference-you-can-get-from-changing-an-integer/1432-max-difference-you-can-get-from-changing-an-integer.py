class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        for c in s:
            if c != '9':
                max_num = int(s.replace(c, '9'))
                break
        else:
            max_num = num
        if s[0] != '1':
            min_num = int(s.replace(s[0], '1'))
        else:
            for c in s[1:]:
                if c not in ('0', '1'):
                    min_num = int(s.replace(c, '0'))
                    break
            else:
                min_num = num
        return max_num - min_num