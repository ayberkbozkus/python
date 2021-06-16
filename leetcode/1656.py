class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.data = [None] * (n+1)
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        
        self.out = []        
        self.data[idKey-1] = value
        while self.data[self.ptr]:
            self.out.append(self.data[self.ptr])
            if self.ptr == self.n-1:
                break
            self.ptr += 1  
        
        return self.out


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)