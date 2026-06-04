class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # create bi directional graph with dict
        # run dfs with cycle detection
        # ensure all nodes visited
        if len(edges) > n-1:
            return False

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visit = set()

        #since this is a dfs with undirected edges we need the
        # parent because we dont want to treat seeing the parent
        # as a cycle
        def dfs(node, par):
            if node in visit:
                return False
            visit.add(node)
            for nei in graph[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visit) == n
        
