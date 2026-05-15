class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjlist = {c:set() for word in words for c in word}


        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            lenw1, lenw2 = len(w1), len(w2)
            minlen = min(lenw1, lenw2)
            if w1[:minlen] == w2[:minlen] and lenw1 > lenw2:
                return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    adjlist[w1[j]].add(w2[j])
                    break
        visit = {} #False = visited True= in current path
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for neigh in adjlist[c]:
                if dfs(neigh):
                    return True
            visit[c] = False
            res.append(c)
        
        for c in adjlist:
            if dfs(c):
                return ""
        return "".join(res[::-1])


