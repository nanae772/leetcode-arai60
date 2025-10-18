# OverflowErrorになってしまう
class SolutionOverFlowError:
    def myPow(self, x: float, n: int) -> float:
        def pow_helper(k: int) -> float:
            if k == 0:
                return 1
            return pow_helper(k // 2) ** 2 * x ** (k % 2)

        if n >= 0:
            return pow_helper(n)
        else:
            return 1 / pow_helper(-n)


class SolutionRecursionBottomUp:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n > 0:
            return self.myPow(x, n // 2) ** 2 * x ** (n % 2)
        else:
            return self.myPow(x, -(-n // 2)) ** 2 / x ** (-n % 2)


class SolutionRecursionTopDown:
    def myPow(self, x: float, n: int) -> float:
        def mypow_helper(x: float, n: int, result: float) -> float:
            if n == 0:
                return result

            if n > 0:
                return mypow_helper(x * x, n // 2, result * x ** (n % 2))
            else:
                return mypow_helper(x * x, -(-n // 2), result / x ** (-n % 2))

        return mypow_helper(x, n, 1.0)


class SolutionIteration:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        while n > 0:
            if n & 1:
                result *= x
            x *= x
            n >>= 1

        return result
