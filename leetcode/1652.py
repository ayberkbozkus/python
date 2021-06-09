class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        tmp_array = []
        
        for i in range(n):
            if k==0:
                tmp_array.append(0)
            elif k>0:
                tmp_array.append(0)
                for y in range(0,k):
                    tmp_array[-1] += code[(i + y + 1) % n]
            else:
                tmp_array.append(0)
                for y in range(k,0):
                    tmp_array[-1] += code[(i + y ) % n]
        return tmp_array