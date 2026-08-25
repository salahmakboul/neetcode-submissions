class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                
                if grid[r][c] == '1':
                    counter += 1
                    self.scout(grid, r, c) 
                    
        return counter

    def scout(self, grid, r, c):
        
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return
            
        if grid[r][c]=='0' :
            return
            
        grid[r][c] = '0'
        
        self.scout(grid, r - 1, c)
        self.scout(grid, r + 1, c) 
        self.scout(grid, r, c - 1) 
        self.scout(grid, r, c + 1)