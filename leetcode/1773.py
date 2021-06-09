class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        out = 0
        if ruleKey == "type":
            for item in items:
                if ruleValue == item[0]:
                    out+=1
        elif ruleKey == "color":
            for item in items:
                if ruleValue == item[1]:
                    out+=1
        else:
            for item in items:
                if ruleValue == item[2]:
                    out+=1
        return out