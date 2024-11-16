class PowerBase:
    def run(self, x_str: str, n_str: str) -> str:
        x_, n_ = float(x_str), int(n_str)
        return str(round(self.power(x_, n_), 11))

    def power(self, x: float, n: int) -> float:
        raise NotImplementedError


class PowerIter(PowerBase):
    """Итеративное возведение в степень"""

    def power(self, x: float, n: int) -> float:
        r = 1.0
        for _ in range(n):
            r *= x
        return r


class PowerRecursion(PowerBase):
    """Возведение в степень через степени двойки"""

    def power(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        r = self.power(x, n // 2)
        return r * r if n % 2 == 0 else x * r * r
