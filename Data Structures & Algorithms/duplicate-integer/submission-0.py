class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ht = {}
        for num in nums:
            if num in ht: # dupe
                return True
            ht[num] = 1 # default
        return False