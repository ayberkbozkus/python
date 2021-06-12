class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        length = len(encoded)
        out = [first for i in range(length+1)]
        for i in range(length):
            out[i+1] = encoded[i] ^ out[i]
        return out