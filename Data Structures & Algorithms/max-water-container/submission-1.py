class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        
        maxAmount = 0
        while i < j:
            totalAmount = (j - i) * min(heights[i], heights[j])
            # print(i, j, totalAmount, heights[i], heights[j])
            if heights[i] < heights[j]:
                i += 1
            elif heights[j] < heights[i]:
                j -= 1
            else:
                i += 1
                j -= 1
            maxAmount = max(maxAmount, totalAmount)
        
        return maxAmount