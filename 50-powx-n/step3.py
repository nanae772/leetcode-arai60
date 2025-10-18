class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            if n == 0:
                return 1
            else:
                return 0

        base = x
        exp = n
        if exp < 0:
            base = 1 / base
            exp = -exp

        result = 1
        while exp > 0:
            if exp % 2 == 1:
                result *= base
            base *= base
            exp //= 2
        return result
