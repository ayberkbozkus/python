class Solution:
    def sortSentence(self, s: str) -> str:
        return " ".join([word[:-1] for word in sorted(s.split(), key = lambda sequence: sequence[-1], reverse=False)])