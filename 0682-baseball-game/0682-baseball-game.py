class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        record,sum=[],0
        for i in operations:
            if i.isdigit() or i[0]=="-":
                record.append(int(i))
            elif i=="C":
                record.pop(-1)
            elif i=="D":
                record.append(int(record[-1])*2)
            elif i=="+":
                record.append(int(record[-1])+int(record[-2]))
        for i in range(len(record)):
            sum+=record[i]
        return sum