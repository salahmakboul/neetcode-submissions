class Solution {
    public int orangesRotting(int[][] grid) {
    Queue<int[]> queue = new LinkedList<>();
    int[][] moves = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
        int freshCount = 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[r].length; c++) {
                if (grid[r][c] == 2) {
                    queue.add(new int[]{r, c});
                }
                if (grid[r][c] == 1) {
                    freshCount++;
                }
            }
        }
        int minutes = 0;
        while (!queue.isEmpty() && freshCount> 0){
            int batchSize= queue.size() ;
            for (int i = 0; i < batchSize; i++) {
                int[] rottenOrange = queue.poll();
                int currR = rottenOrange[0]; 
                int currC = rottenOrange[1]; 
                for (int[] move : moves) {
                    int newR = currR + move[0];
                    int newC = currC + move[1];

                    if (newR >= 0 && newR < grid.length && newC >= 0 && newC < grid[0].length && grid[newR][newC] == 1) {
                        grid[newR][newC] = 2;       
                        freshCount--;         
                        queue.offer(new int[]{newR, newC}); 
                    }
                }
            }
            minutes+=1;
        }
        if (freshCount == 0) {
            return minutes ;
        }
        
        return -1;
    }
}
