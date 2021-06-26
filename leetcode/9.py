class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if abs(x) != x:
            return False
        elif "".join([num for num in str(x)]) != "".join(reversed([num for num in str(x)])):
            return False
        return True