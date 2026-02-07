class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        L=[]    
        for i in range(len(code)):  
            if(code[i].isalnum() or '_' in code[i])and code[i]!=''and businessLine[i] in ["electronics","grocery","pharmacy","restaurant"] and isActive[i]: L.append((businessLine[i],code[i]))
        business_line_order={"electronics":1,"grocery":2,"pharmacy":3,"restaurant":4} 
        L.sort(key=lambda x:(business_line_order[x[0]],x[1]))  
        result=[coupon[1] for coupon in L]  
        return result