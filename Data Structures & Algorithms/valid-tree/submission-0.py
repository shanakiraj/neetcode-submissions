class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        #create bi directional graph with dict
        # run dfs with cycle detection
        # ensure all nodes visited
        if len(edges) > n-1:
            return False

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visit = set()

        def dfs(cur, par):
            if cur in visit:
                return False
            visit.add(cur)
            for node in graph[cur]:
                if node == par:
                    continue
                if not dfs(node, cur):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n
        
