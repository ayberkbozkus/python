class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        out = "".join(reversed([num for num in str(x)]))
        
        if str(x)[0] == "-":
            out = "-" + out[:len(out)-1]
        if abs(int(out)) > 2147483647:
            out = "0"
        return int(out)