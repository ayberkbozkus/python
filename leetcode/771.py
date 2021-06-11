class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        out = 0
        for i in jewels:
            for j in stones:
                if i == j:
                    out += 1
        return out