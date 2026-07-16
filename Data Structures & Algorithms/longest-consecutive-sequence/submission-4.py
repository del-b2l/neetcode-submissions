class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0

        for n in numSet:
            # check whether n is start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while n + length in numSet:
                    # print(n + length)
                    length += 1
                # compute max sequence
                # print(f"length: {length}")
                maxLength = max(length, maxLength)
                # print(f"maxLength: {maxLength}\n")
        
        return maxLength