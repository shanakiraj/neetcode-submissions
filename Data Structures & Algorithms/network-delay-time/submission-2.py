class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        # start from source node, bfs until target node is met
        # use a minheap to pop the min weight edge at a time
        # return once we find k

        
        adjlist = defaultdict(list)

        for u, v, t in times:
            adjlist[u].append((t, v))
        minHeap = [(0, k)]
        visit = set()
        res = 0

        while minHeap:
            t1, u = heapq.heappop(minHeap)

            if u in visit:
                continue
            visit.add(u)
            res = max(res, t1)

            for t2, v in adjlist[u]:
                heapq.heappush(minHeap, (t1+t2, v))
        return res if len(visit) == n else -1

        













            