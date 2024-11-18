from primes import PrimesBase, PrimesIter
from test_primes import Test

if __name__ == "__main__":

    def test():
        test = Test(power.run)
        test.run()

    print("Итеративное вычисление степени")

    power: PrimesBase = PrimesIter()
    test()
