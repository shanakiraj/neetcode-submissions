class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]


        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if (row in range(rows) and
                    col in range(cols) and
                    grid[row][col] == INF):
                    grid[row][col] = grid[r][c] + 1
                    q.append((row,col))



                    