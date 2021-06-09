class Solution:
    def interpret(self, command: str) -> str:
        temp = ""
        result = ""
        for i in command:
            temp += i
            if temp == "G":
                temp = ""
                result += "G"
            elif temp == "()":
                temp = ""
                result += "o"
            elif temp == "(al)":
                temp = ""
                result += "al"
        return result