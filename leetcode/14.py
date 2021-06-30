class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        print(strs)
        out = ""
        if len(strs)==0: return ""
        if len(strs)==1: return strs[0]
        
        for letter in range(len(min(strs))):
            if min(strs)[letter] == strs[1][letter] and min(strs)[letter] == max(strs)[letter]:
                out += strs[0][letter]
                continue
            break
        return out