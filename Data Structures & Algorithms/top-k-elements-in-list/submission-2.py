class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {} # number -> frequency
        
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
        # print(frequency)

        n = len(nums)
        count = [[] for _ in range(n + 1)] # lists we'll store values in acc. to freq.
        # print(count)

        for num, freq in frequency.items():
            count[freq].append(num)
        
        # traverse backward to retrieve top k elements
        result = []
        for i in range(len(count) - 1, -1, -1):
            if count[i] != []:
                for num in count[i]:
                    result.append(num)
                    if len(result) == k:
                        return result