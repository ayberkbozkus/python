class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        l = len(accounts)
        wealth = [0 for i in range(l)]
        for i in range(l):
            for j in accounts[i]:
                wealth[i]+=j
        
        return max(wealth)