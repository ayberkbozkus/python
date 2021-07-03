# The best solution I have seen
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         d = {}
#         for i, num in enumerate(nums):
#             if num in d:
#                 return i, d[num]
#             else:
#                 diff = target - num
#                 d[diff] = i

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)-1-i):
                if nums[i] + nums[j+i+1] == target:
                    return [i,i+j+1]

# recursive solution better performance than for loop
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         self.first = 0
#         self.target = target
#         self.nums = nums
#         self.counter = 0
#         def traveler(tmp,check):
#             if check:
#                 if (self.nums[self.first] + self.nums[tmp]) == self.target:
#                     return [self.first + self.counter, tmp + self.counter]
#                 else:
#                     return traveler(tmp+1,True)
#             elif (self.target - self.nums[tmp]) in self.nums[1:]:
#                 self.first = tmp
#                 return traveler(tmp+1,True)
#             else:
#                 self.counter +=1
#                 del self.nums[0]
#                 return traveler(tmp, False)
       
#         return traveler(0,False)


