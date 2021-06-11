class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = [ 0 for i in range(len(nums)) ] 
        for i in range(len(nums)):
            for j in range(i+1):
                temp[i]+=nums[j]
                
        return temp