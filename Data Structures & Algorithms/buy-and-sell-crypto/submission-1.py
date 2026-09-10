class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        min_price = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            profit = prices[i] - min_price
            max_profit = max(max_profit, profit)

    
        return max_profit
