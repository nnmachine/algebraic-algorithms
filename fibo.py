from math import sqrt

from power import PowerIter


class FiboBase:
    def run(self, n_str: str) -> str:
        n_ = int(n_str)
        return str(self.fibo(n_))

    def fibo(self, n: int) -> int:
        raise NotImplementedError


class FiboRecursion(FiboBase):
    def fibo(self, n: int) -> int:
        if n == 0:
            return 0
        if n in (1, 2):
            return 1
        return self.fibo(n - 1) + self.fibo(n - 2)


class FiboIter(FiboBase):
    def fibo(self, n: int) -> int:
        if n == 0:
            return 0
        if n in (1, 2):
            return 1

        f1, f2 = 1, 1

        for _ in range(2, n):
            f_tmp = f1
            f1 = f2
            f2 = f_tmp + f1
        return f2


class FiboGoldenRatio(FiboBase):
    pow_ = PowerIter().power

    def fibo(self, n: int) -> int:
        try:
            fi = (1.0 + sqrt(5)) / 2.0
            f = int(self.pow_(fi, n) / sqrt(5) + 0.5)
        except OverflowError:
            f = -1
        return f
