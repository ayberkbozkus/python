class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_num = 0
        l_num = 0
        num = 0
        for i in s:
            if i == 'R':
                r_num += 1
            else:
                l_num += 1
            if r_num == l_num:
                num+=1
        
        return num