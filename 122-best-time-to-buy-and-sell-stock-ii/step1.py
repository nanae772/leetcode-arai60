# O(N)だが間違っている
class SolutionWA:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        max_price = prices[0]
        min_price = prices[0]
        for price in prices:
            if price >= min_price:
                max_price = max(max_price, price)
                continue

            max_profit += max_price - min_price
            max_price = price
            min_price = price

        max_profit += max_price - min_price
        return max_profit


# dp[i][j] = (i日目における売り(j=0)/買い(j=1)をしたときの利益) とする
# O(N^2)なのでTLE
class SolutionWithTLE:
    def maxProfit(self, prices: list[int]) -> int:
        num_days = len(prices)
        dp = [[0] * 2 for _ in range(num_days)]
        for i in range(1, num_days):
            dp[i][0] = max(dp[j][1] + prices[i] - prices[j] for j in range(i))
            dp[i][1] = max(dp[j][0] for j in range(i))

        return max(dp[num_days - 1])


# dp[i][j] = (i日目における売り(j=0)/買い(j=1)をしたときの所持金) とする
# O(N^2)なのでTLE
class SolutionWithTLE2:
    def maxProfit(self, prices: list[int]) -> int:
        num_days = len(prices)
        dp = [[0] * 2 for _ in range(num_days)]
        dp[0][1] = -prices[0]
        for i in range(1, num_days):
            dp[i][0] = prices[i] + max(dp[j][1] for j in range(i))
            dp[i][1] = -prices[i] + max(dp[j][0] for j in range(i))

        # 最後の買いはただ損なだけなので無かったことにする
        return max(dp[num_days - 1][0], dp[num_days - 1][1] + prices[-1])


# O(N)で正しい解法
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_bought_previous = -prices[0]
        max_sold_previous = 0
        for price in prices[1:]:
            max_bought_previous, max_sold_previous = (
                max(max_bought_previous, max_sold_previous - price),
                max(max_sold_previous, max_bought_previous + price),
            )
        # 最後の買いは損なだけなので無かったことにする
        result = max(max_bought_previous + prices[-1], max_sold_previous)
        return result
