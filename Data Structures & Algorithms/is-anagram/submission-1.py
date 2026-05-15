class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        for c in s:
            dictS[c] = dictS.get(c, 0) + 1
        for c in t:
            if dictS.get(c, 0) == 0:
                return False
            dictS[c] -= 1
        
        return sum(dictS.values()) == 0

