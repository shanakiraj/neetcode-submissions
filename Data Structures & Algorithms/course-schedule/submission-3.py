class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        adjlist = defaultdict(list)
        visiting = set()

        for u, v in prerequisites:
            adjlist[u].append(v)
        
        def dfs(node):
            if node in visiting:
                return False
            if adjlist[node] == []:
                return True
            visiting.add(node)

            for nei in adjlist[node]:
                if not dfs(nei):
                    return False
            visiting.remove(node)
            adjlist[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True