class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        out = 0
        for i in range(n):
            out ^= (start + i*2)
        return out