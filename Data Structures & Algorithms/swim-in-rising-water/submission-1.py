class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        N = len(grid)-1
        directions = [[1,0], [-1, 0], [0,1], [0, -1]]
        minHeap = [(grid[0][0], 0, 0)]
        visit = set()
        while minHeap:
            t, r1, c1 = heapq.heappop(minHeap)

            if (r1, c1) in visit:
                continue
            if r1 == N and c1 == N:
                return t

            visit.add((r1, c1))
            
            for dr, dc in directions:
                r2, c2 = r1+dr, c1+dc
                if (r2 < 0 or c2 < 0 or
                    r2 > N or c2 > N or
                    (r2, c2) in visit):
                    continue
                heapq.heappush(minHeap, (max(t, grid[r2][c2]), r2, c2))
        



