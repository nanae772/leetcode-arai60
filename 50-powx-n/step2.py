class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            if n == 0:
                return 1.0
            else:
                return 0

        if n < 0:
            x = 1 / x
            n = -n
        result = 1.0
        base = x
        exp = n
        while exp > 0:
            if exp % 2 == 1:
                result *= base
            base *= base
            exp //= 2
        return result
