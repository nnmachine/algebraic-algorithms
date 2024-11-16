class Euclid:
    def run(self, m_str: str, n_str: str) -> str:
        n_ = int(n_str)
        m_ = int(m_str)
        return str(self.gcd(m_, n_))

    def gcd(self, m: int, n: int) -> int:
        raise NotImplementedError


class EuclidRecursion(Euclid):
    def gcd(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 1
        if m == n:
            return m
        if m > n:
            return self.gcd(n, m - n)
        else:
            return self.gcd(m, n - m)


class EuclidRecursionMod(Euclid):
    def gcd(self, m: int, n: int) -> int:
        if n == 0:
            if m:
                return m
            else:
                return 1
        elif m == 0:
            return n

        if m == n:
            return m

        if m > n:
            return self.gcd(n, m % n)
        else:
            return self.gcd(m, n % m)
