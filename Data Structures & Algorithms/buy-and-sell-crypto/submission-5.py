class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0] # keep track of minimum buy price
        maxProfit = 0

        for sell in prices[1:]: # from index 1
            # buy = min(prices[:i]) | from index 0 to i - 1, but this results in TLE :<
            minBuy = min(sell, minBuy)
            maxProfit = max(maxProfit, sell - minBuy)
        
        return maxProfit