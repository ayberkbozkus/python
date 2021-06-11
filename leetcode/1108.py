class Solution:
    def defangIPaddr(self, address: str) -> str:
        ips = address.split(".")
        l = len(ips)
        out = ""
        for i in range(l):
            if i == l-1:
                out += ips[i]
                break
            out += ips[i] + "[.]"
        return out