class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sumd = 0
        for i in str(n):
            product *= int(i)
            sumd += int(i)
        return product-sumd