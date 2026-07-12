class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        equality = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in equality:
                return [equality[difference], i]
            equality[nums[i]] = i # value: index, complement we expect l8r