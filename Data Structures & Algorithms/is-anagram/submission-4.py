class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = collections.defaultdict(int)

        if len(s) != len(t):
            return False
        for c in s:
            dictS[c] += 1
        for c in t:
            if dictS[c] == 0:
                return False
            dictS[c] -= 1
        

        return True