from primes import PrimesBase, PrimesIter, PrimesEratosthen
from test_primes import Test

if __name__ == "__main__":

    def test():
        test = Test(power.run)
        test.run()

    print("Поиск количества простых чисел через итерации с оптимизациями")

    power: PrimesBase = PrimesIter()
    test()

    print("Поиск колличества простых чисел через решето Эратосфена")

    power: PrimesBase = PrimesEratosthen()
    test()
