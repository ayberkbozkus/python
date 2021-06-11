class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        out = ""
        temp = [0 for i in range(len(s))]
        for i in range(len(s)):
            temp[indices[i]] = s[i]
        for i in temp:
            out +=i
        return out