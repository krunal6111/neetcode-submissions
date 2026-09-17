class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # Extract the integer of length as string
            res.append(s[j + 1:j + 1 + length])
            i = j + 1 + length # Now i will be at the position of the integer with denotes the length of the upcoming string

        return res
            
        

