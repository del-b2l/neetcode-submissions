class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0

        for n in nums:
            # check whether n is start of a sequence
            if (n - 1) not in numSet:
                length = 0
                # if true, keep expanding it
                nextNum = n
                while nextNum in numSet:
                    print(nextNum)
                    nextNum += 1
                    length += 1
                # compute max sequence
                print(f"length: {length}")
                maxLength = max(length, maxLength)
                print(f"maxLength: {maxLength}\n")
        
        return maxLength