class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)-1-i):
                if nums[i] + nums[j+i+1] == target:
                    return [i,i+j+1]