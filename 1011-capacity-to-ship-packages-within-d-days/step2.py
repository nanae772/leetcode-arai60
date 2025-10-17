class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        if days <= 0:
            raise ValueError(f"days must be positive. {days=}")
        if not weights:
            raise ValueError("weights must not be empty.")

        def can_ship_within_days(capacity: int) -> bool:
            required_days = 1
            loaded_weight = 0
            for weight in weights:
                if loaded_weight + weight > capacity:
                    required_days += 1
                    loaded_weight = weight
                    continue
                loaded_weight += weight

            return required_days <= days

        low = max(weights) - 1
        high = sum(weights)
        while low + 1 < high:
            mid = (low + high) // 2
            if can_ship_within_days(mid):
                high = mid
            else:
                low = mid

        return high
