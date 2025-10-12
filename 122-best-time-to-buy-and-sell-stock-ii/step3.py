class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        max_profit = 0
        price_yesterday = prices[0]
        for price in prices:
            if price > price_yesterday:
                max_profit += price - price_yesterday
            price_yesterday = price

        return max_profit
