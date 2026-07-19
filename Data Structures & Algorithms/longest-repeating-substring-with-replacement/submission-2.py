class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # A - Z, frequency
        result = 0 # size of the window
        l = 0

        maxFreq = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(maxFreq, count[s[r]])

            while (r - l + 1) - maxFreq > k: # our stopping condition
                count[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
        
        return result