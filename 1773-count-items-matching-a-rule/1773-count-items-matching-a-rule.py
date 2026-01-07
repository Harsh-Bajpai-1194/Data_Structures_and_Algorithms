class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        if ruleKey=="type": index=0
        if ruleKey == "color": index=1
        if ruleKey == "name": index=2
        c=0
        for i in items:
            if ruleValue==i[index]: c+=1
        return c