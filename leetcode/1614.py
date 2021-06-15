class Solution:
    def maxDepth(self, s: str) -> int:
        self.max = 0
        self.count = 0
        for i in s:
            if i == "(":
                self.count += 1
            if i == ")":
                self.count -= 1
            if self.max < self.count:
                self.max = self.count
                
        return self.max