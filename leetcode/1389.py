class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        length = len(index)
        out = []
        for i in range(length):
            out.insert(index[i], nums[i])
        return out