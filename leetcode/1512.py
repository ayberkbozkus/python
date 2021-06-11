class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        out = 0
        l = len(nums)
        for i in range(l):
            for j in range(l-i-1):
                if nums[i] == nums[-j-1]:
                    out +=1
        return out