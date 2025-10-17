class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        if days <= 0:
            raise ValueError(f"days must be positive. {days=}")
        if not weights:
            raise ValueError("weights must not be empty.")

        def can_ship(capacity: int) -> bool:
            if capacity < max(weights):
                return False

            required_days = 1
            loaded_weight = 0
            for weight in weights:
                if loaded_weight + weight > capacity:
                    required_days += 1
                    loaded_weight = weight
                    continue
                loaded_weight += weight

            return required_days <= days

        max_capacity_cant_ship = 0
        min_capacity_can_ship = sum(weights)
        while max_capacity_cant_ship + 1 < min_capacity_can_ship:
            capacity = (max_capacity_cant_ship + min_capacity_can_ship) // 2
            if can_ship(capacity):
                min_capacity_can_ship = capacity
            else:
                max_capacity_cant_ship = capacity

        return min_capacity_can_ship
