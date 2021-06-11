class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l = len(candies)
        out = [True for i in range(l)]
        
        for i in range(l):
            print(candies[i] + extraCandies," - ",max(candies))
            if (candies[i] + extraCandies) < max(candies):
                out[i] = False
        
        return out