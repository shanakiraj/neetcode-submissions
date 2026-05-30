class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        visit = set()
        adjlist = defaultdict(list)

        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)

        def dfs(node):
            for nei in adjlist[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)
        res = 0 
        for i in range(n):
            if i not in visit:
                visit.add(i)
                dfs(i)
                res += 1
        return res

