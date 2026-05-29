class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prereqs = defaultdict(list)


        for crs, pre in prerequisites:
            prereqs[crs].append(pre)

        output = []


        visiting, visited = set(), set()

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            
            visiting.add(crs)

            for pre in prereqs[crs]:
                if dfs(pre) == False:
                    return False
            visiting.remove(crs)
            visited.add(crs)

            output.append(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output












