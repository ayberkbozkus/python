class Solution(object):
    def romanToInt(self, s):
        roman = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        """
        :type s: str
        :rtype: int
        """
        out = 0
        for i in range(len(s)):
            
            out += roman[s[i]]
            
            if i == len(s) -1:
                break
            if s[i] == "I":
                if s[i+1] == "V" or s[i+1] == "X":              
                    out -= 2
            if s[i] == "X":
                if s[i+1] == "L" or s[i+1] == "C":
                    out -= 20
            if s[i] == "C":
                if s[i+1] == "D" or s[i+1] ==  "M":
                    out -= 200
        return out