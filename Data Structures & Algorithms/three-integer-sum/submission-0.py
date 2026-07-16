class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            a = nums[i]
            if a > 0: # sum can never be 0 this way
                break

            if i > 0 and a == nums[i - 1]: # skipping dupes
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else: # threeSum == 0
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
        return result
        # print(nums)