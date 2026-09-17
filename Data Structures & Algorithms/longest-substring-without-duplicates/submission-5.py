class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l = 0
        longest = 1
        charSet = set()
        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[l])
                l += 1 
            charSet.add(s[i])
            longest = max(longest, len(charSet)) 

        return longest
        