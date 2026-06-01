class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjlist = defaultdict(list)

        for u, v, w in times:
            adjlist[u].append((v, w))
        

        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            w1, u = heapq.heappop(minHeap)

            if u in visit:
                continue
            
            visit.add(u)
            
            t = max(t, w1)

            for v, w2 in adjlist[u]:
                if v not in visit:
                    heapq.heappush(minHeap, (w1+w2, v))
        return t if len(visit) == n else -1
