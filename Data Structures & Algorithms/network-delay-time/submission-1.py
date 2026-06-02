class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        # start from source node, bfs until target node is met
        # use a minheap to pop the min weight edge at a time
        # return once we find k

        
        adjlist = defaultdict(list)
        visit = set()
        res = 0
        for u, v, t in times:
            adjlist[u].append((t, v))
        
        minHeap = [(0, k)]

        while minHeap:
            t, u = heapq.heappop(minHeap)

            #we have already processed the node with its min
            #edge so we have a faster way to get to it
            if u in visit:
                continue
            visit.add(u)
            res = max(t, res)

            for t2, v in adjlist[u]:
                heapq.heappush(minHeap, (t+t2, v))
        return res if len(visit) == n else -1
        













            