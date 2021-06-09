class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        temp = [ [ 0 for i in range(n) ] for j in range(m) ]
        for i in range(k):
            for x in range(m):
                temp[x] = grid[x][n-1:] + grid[x][:n-1]
                grid[x] = temp[x][:1]+ temp[x][1:]
            for x in range(m):
                if x+1 == m:
                    grid[0][0] = temp[-1][0]
                    
                else:
                    grid[x+1][0] = temp[x][0]
                    
            
        return grid