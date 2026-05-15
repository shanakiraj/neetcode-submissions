class Solution:
    def __init__(self):
        self.dirs = [[1,0],[0,1],[-1,0],[0,-1]]

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        res = 0

        def bfs(r, c):
            total = 1
            q = deque([(r,c)])
            while q:
                r, c = q.popleft()
                for dr, dc in self.dirs:
                    row, col = r+dr, c+dc

                    if (0 <= row < rows and
                        0 <= col < cols and
                        (row,col) not in visit and
                        grid[row][col] == 1):
                        visit.add((row,col))
                        total += 1
                        q.append((row,col))
            return total
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == 1:
                    visit.add((r,c))
                    res = max(res, bfs(r,c))
        return res
    
        

        


