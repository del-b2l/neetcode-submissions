class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        # prefixes
        for i in range(1, len(nums)):
            output[i] = nums[i - 1] * output[i - 1]
        print(output)

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * suffix
            suffix = suffix * nums[i]
        return output