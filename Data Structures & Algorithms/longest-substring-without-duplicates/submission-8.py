class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
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
        """

        # more optimal sol: hash map
        # jump the left pointer directly to the correct position
        uniqueChars = {} # stores last index for each char appeared
        res = 0
        l = 0

        for r in range(len(s)):
            if s[r] in uniqueChars:
                l = max(uniqueChars[s[r]] + 1, l) # l shouldn't move backwards
            uniqueChars[s[r]] = r # last occurrence's index
            res = max(res, r - l + 1)
        
        return res