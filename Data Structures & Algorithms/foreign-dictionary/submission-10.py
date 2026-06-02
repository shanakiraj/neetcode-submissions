class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        

        adjlist = {c: set() for w in words for c in w}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]

            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adjlist[w1[j]].add(w2[j])
                    break
        
        visited = set()
        visiting = set()
        res = []

        def dfs(char):
            if char in visited:
                return False
            if char in visiting:
                return True
            
            visiting.add(char)

            for nei in adjlist[char]:
                if dfs(nei):
                    return True
                    
            visited.add(char)
            visiting.remove(char)
            res.append(char)
        
        for c in adjlist:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)

