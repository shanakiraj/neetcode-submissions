class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        prereqs = defaultdict(list)

        for crs, pre in prerequisites:
            prereqs[crs].append(pre)
        
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if prereqs[crs] == []:
                return True
            
            visiting.add(crs)
            for pre in prereqs[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            prereqs[crs] = []
            return True

        
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True