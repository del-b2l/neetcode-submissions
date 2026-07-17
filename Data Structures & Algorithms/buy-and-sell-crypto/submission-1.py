class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i, sell in enumerate(prices, start = 1): # start @ index 1
            buy = min(prices[:i]) # from index 0 to i - 1
            if buy >= sell:
                continue
            maxProfit = max(sell - buy, maxProfit)
        return maxProfit