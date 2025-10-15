import collections
import math


# DP解
class SolutionDP:
    def coinChange(self, coins: list[int], amount: int) -> int:
        filtered_coins = [coin for coin in coins if coin <= amount]
        sorted_coins = sorted(filtered_coins)
        min_required_coins = [math.inf] * (amount + 1)
        min_required_coins[0] = 0

        for remainder in range(1, amount + 1):
            for coin in sorted_coins:
                if coin > remainder:
                    break
                min_required_coins[remainder] = min(
                    min_required_coins[remainder],
                    1 + min_required_coins[remainder - coin],
                )

        if min_required_coins[amount] == math.inf:
            return -1

        return min_required_coins[amount]


# 最短経路問題とみなしてBFSで解く
class SolutionBFS:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount < 0:
            raise ValueError(f"amount must not be negative: {amount=}")

        filtered_coins = [coin for coin in coins if coin <= amount]
        sorted_coins = sorted(filtered_coins, reverse=True)
        money_count_pairs = collections.deque([(0, 0)])
        is_checked = [False] * (amount + 1)
        is_checked[0] = True

        while money_count_pairs:
            money, count = money_count_pairs.popleft()
            if money == amount:
                return count

            for coin in sorted_coins:
                added_money = money + coin
                if added_money > amount:
                    continue
                if is_checked[added_money]:
                    continue
                money_count_pairs.append((added_money, count + 1))
                is_checked[added_money] = True

        return -1
