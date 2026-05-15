class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        #dfs O(V+E) 
        adjlist = {src:[] for src in range(n)}

        for src, dst in edges:
            adjlist[src].append(dst)
            adjlist[dst].append(src)
        res = 0
        
        
        visit = set()
        def dfs(node):
            if node in visit:
                return 0
            visit.add(node)
            for neigh in adjlist[node]:
                if neigh not in visit:
                    dfs(neigh)
            return 1
        for i in range(n):
            res += dfs(i)
        return res