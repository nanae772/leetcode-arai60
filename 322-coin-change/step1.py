class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount < 0:
            raise ValueError(f"amount must not be negative: {amount=}")

        min_required_coins = [float("inf")] * (amount + 1)
        min_required_coins[0] = 0
        for remain in range(1, amount + 1):
            for coin in coins:
                if remain < coin:
                    continue
                min_required_coins[remain] = min(
                    min_required_coins[remain],
                    1 + min_required_coins[remain - coin],
                )

        if min_required_coins[amount] == float("inf"):
            return -1

        return min_required_coins[amount]
