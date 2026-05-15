class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj = {c:set() for word in words for c in word}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minlen = min(len(w1), len(w2))
            if w1[:minlen] == w2[:minlen]:
                if len(w1) > len(w2):
                    return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit = {}
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True #in path
            for neigh in adj[c]:
                if dfs(neigh):
                    return True
            visit[c] = False #no longer in path but is visited
            res.append(c)
        for c in adj:
            if dfs(c):
                return ""
        return "".join(res[::-1])



