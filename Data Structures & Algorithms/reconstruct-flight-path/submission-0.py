class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        tickets.sort()
        adj = defaultdict(list)

        for u, v in tickets:
            adj[u].append(v)
        
        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets)+1:
                return True
            if src not in adj:
                return False
            
            nodes = list(adj[src])
            for i, v in enumerate(nodes):
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True
                res.pop()
                adj[src].insert(i, v)
            return False
        dfs("JFK")
        return res

