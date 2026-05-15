class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += (str(len(word)) + "#" + word)
        return res
            

    def decode(self, s: str) -> List[str]:
        #step through the string until you find a #
        #grab from that point to the beginning of the end point
        #convert to int
        #grab from the next point until the length of that string
        #set the next value as the end point
        #continue
        res = []
        i = 0
        j = 0
        while j < len(s):
            i = j
            while s[i] != "#":
                i += 1
            length = int(s[j:i])

            #moves j to the first number of next word
            j = i + length +1
            res.append(s[i+1:j])
            

        return res



