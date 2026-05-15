class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        par = [i for i in range(n)]
        rank = [1]*n

        #union find
        def find(n):
            res = n
            while res != par[res]:
                #par[n] = par[par[n]]
                res = par[n]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res


        #dfs O(V+E) 
        # adjlist = {src:[] for src in range(n)}

        # for src, dst in edges:
        #     adjlist[src].append(dst)
        #     adjlist[dst].append(src)
        # res = 0
        
        
        # visit = set()
        # def dfs(node):
        #     if node in visit:
        #         return 0
        #     visit.add(node)
        #     for neigh in adjlist[node]:
        #         if neigh not in visit:
        #             dfs(neigh)
        #     return 1
        # for i in range(n):
        #     res += dfs(i)
        # return res

