class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l = len(nums)
        temp = 0
        out = []
        for i in range(l):
            if i%2 == 1:
                print(temp)
                for j in range(temp):
                    out.append(nums[i])
            temp = nums[i]
        return out
                