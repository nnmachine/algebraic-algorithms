from math import sqrt


class PrimesBase:
    def run(self, n_str: str) -> str:
        n_ = int(n_str)
        return str(self.primes(n_))

    def primes(self, n: int) -> int:
        raise NotImplementedError


class PrimesIter(PrimesBase):
    def primes(self, n: int) -> int:
        if n in (0, 1):
            return 0
        cnt = 0
        for n_ in range(2, n+1):
            if self.__is_prime(n_):
                cnt += 1
        return cnt

    def __is_prime(self, n: int) -> bool:
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        for x in range(3, int(sqrt(n))+1, 2):
            if n % x == 0:
                return False

        return True


class PrimesEratosthen(PrimesBase):
    def primes(self, n: int) -> int:
        if n in (0, 1):
            return 0

        sieve = [False] * (n+1)
        cnt = 0

        for i in range(2, n+1):
            if sieve[i] is False:
                cnt += 1
                for j in range(i*i, n+1, i):
                    sieve[j] = True
        return cnt
