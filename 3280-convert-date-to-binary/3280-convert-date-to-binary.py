class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        date=date.split("-")
        return bin(int(str(date[0])))[2:]+"-"+bin(int(str(date[1])))[2:]+"-"+bin(int(str(date[2])))[2:]