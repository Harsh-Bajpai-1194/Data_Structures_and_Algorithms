class Solution(object):
    def majorityFrequencyGroup(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        for i in s: d[i] = d[i] + 1 if i in d else 1
        groups = {}
        for i, count in d.items():
            groups[count] = groups[count] + [i] if count in groups else [i]
        max_size = max_freq = 0
        result = []
        for k, chars in groups.items():
            if len(chars) > max_size or (len(chars) == max_size and k > max_freq):
                max_size, max_freq, result = len(chars), k, chars
        return ''.join(result)