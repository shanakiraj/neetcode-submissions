class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)

        parent = [i for i in range(n+1)]
        rank = [1]*(n+1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            ca = find(a)
            cb = find(b)

            if ca == cb:
                return True
            
            if rank[ca] > rank[cb]:
                parent[cb] = ca
                rank[ca] += rank[cb]
            else:
                parent[ca] = cb
                rank[cb] += rank[ca]
            return 
        
        for u, v in edges:
            if union(u, v):
                return [u, v]


        