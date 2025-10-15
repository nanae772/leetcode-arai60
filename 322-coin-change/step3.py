import math


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount < 0:
            raise ValueError(f"amount must be non-negative: {amount=}")

        min_required_coins = [math.inf] * (amount + 1)
        min_required_coins[0] = 0

        for remainder in range(1, amount + 1):
            for coin in coins:
                if remainder < coin:
                    continue
                min_required_coins[remainder] = min(
                    min_required_coins[remainder],
                    1 + min_required_coins[remainder - coin],
                )

        if min_required_coins[amount] == math.inf:
            return -1

        return min_required_coins[amount]
