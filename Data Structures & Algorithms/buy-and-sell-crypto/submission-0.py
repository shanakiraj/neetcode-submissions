class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0 
        profit = 0

        for r in range(len(prices)):
            diff = prices[r] - prices[l]

            if diff < 0:
                diff = 0
                l = r
            profit = max(profit, diff)
        return profit
        