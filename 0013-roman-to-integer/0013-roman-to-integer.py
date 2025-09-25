class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        deger = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
        res = 0
        i = 0

        while i < len(s):
            num1 = deger[s[i]]
            if i + 1 < len(s):
                num2 = deger[s[i+1]]
                if num1 >= num2:
                    res += num1
                else:
                    res += (num2 - num1)
                    i+=1
            else:
                res += num1
            i+=1
                
        return res