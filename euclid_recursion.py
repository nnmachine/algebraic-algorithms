class Solver:
    def run(self, m_str: str, n_str: str) -> str:
        n_ = int(n_str)
        m_ = int(m_str)
        return str(self.gcd(m_, n_))

    def gcd(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 1
        if m == n:
            return m
        if m > n:
            return self.gcd(n, m - n)
        else:
            return self.gcd(m, n - m)
