class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        self.letters = {'a', 'q', 'm', 'n', 'd', 't', 'g', 'i', 'h', 'v', 'c', 'u', 'e', 'z', 'j', 'x', 'p', 'y', 'k', 'b', 's', 'f', 'w', 'r', 'l', 'o'}
        self.out = set()
        for i in sentence:
            self.out.add(i)
        return self.letters == self.out