class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        out = []
        temp = 0
        for i in nums:
            for j in nums:
                if i>j:
                    temp +=1
                    
            out.append(temp)
            temp = 0
            
        return out
                    