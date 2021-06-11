class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter=0
        while num>0:
            counter +=1
            if num%2 == 1:
                num -=1
                continue
            num/=2
        return counter