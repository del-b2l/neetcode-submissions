class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueChars = set()
        res = 0
        l = 0
        
        for r in range(len(s)): # ensures r doesn't go out of bounds
            while s[r] in uniqueChars:
                uniqueChars.remove(s[l])
                l += 1
            uniqueChars.add(s[r])
            res = max(res, r - l + 1)

        return res