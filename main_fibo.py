import sys

from fibo import FiboBase, FiboIter, FiboRecursion
from test_fibo import Test

if __name__ == "__main__":
    sys.set_int_max_str_digits(10000000)

    def test():
        test = Test(fibo.run)
        test.run()

    print("Итеративное вычисление числа Фибоначчи")

    fibo: FiboBase = FiboIter()
    test()

    print("==============================")
    print("Рекурсивное вычисление чисел Фибоначчи")

    fibo = FiboRecursion()
    test()
