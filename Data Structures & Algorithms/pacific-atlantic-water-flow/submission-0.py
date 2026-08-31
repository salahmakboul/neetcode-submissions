class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(row,col,visited_set,prev_height) :
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            if (row, col) in visited_set:
                return
            if heights[row][col] < prev_height:
                return
            visited_set.add((row, col))
            dfs(row+1 , col ,visited_set,heights[row][col])
            dfs(row-1 , col ,visited_set,heights[row][col])
            dfs(row , col+1 ,visited_set,heights[row][col])
            dfs(row , col-1 ,visited_set,heights[row][col])
        
        rows = len(heights)
        cols = len(heights[0])
        pacific_reach = set()
        atlantic_reach = set()
        result=[]
        for c in range(cols):
            dfs(0, c, pacific_reach,heights[0][c]) 

        for r in range(rows):
            dfs(r, 0, pacific_reach,heights[r][0]) 
        for c in range(cols) :
            dfs(rows-1, c ,atlantic_reach,heights[rows-1][c] )
        for r in range (rows) :
            dfs(r,cols-1,atlantic_reach,heights[r][cols-1])
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_reach and (r, c) in atlantic_reach:
                    result.append([r, c])
        return result
            
        