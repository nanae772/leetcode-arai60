# DP的アプローチ
class SolutionDP:
    def maxProfit(self, prices: list[int]) -> int:
        max_with_stock = -prices[0]
        max_without_stock = 0
        for price in prices[1:]:
            max_with_stock_now = max_without_stock - price
            max_without_stock_now = max_with_stock + price
            max_with_stock = max(max_with_stock, max_with_stock_now)
            max_without_stock = max(max_without_stock, max_without_stock_now)

        return max_without_stock


# アップトレンドが終わったタイミングで売る解法
# ついでに最小取引回数も求める
class SolutionSimple:
    def maxProfit(self, prices: list[int]) -> int:
        price_yesterday = prices[0]
        min_price = prices[0]
        max_profit = 0
        min_trade_num = 0
        for price in prices[1:]:
            if price_yesterday <= price:
                price_yesterday = price
                continue

            max_profit += price_yesterday - min_price
            min_trade_num += 1
            min_price = price
            price_yesterday = price

        if min_price < price_yesterday:
            max_profit += price_yesterday - min_price
            min_trade_num += 1

        return max_profit


# itertools.pairwiseを使ってワンライナーっぽく
class SolutionOneLine:
    def maxProfit(self, prices: list[int]) -> int:
        return sum(
            price_tomorrow - price
            for price, price_tomorrow in itertools.pairwise(prices)
            if price_tomorrow > price
        )
