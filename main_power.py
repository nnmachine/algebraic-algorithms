from power import PowerBase, PowerIter, PowerRecursion
from test_power import Test

if __name__ == "__main__":

    def test():
        test = Test(power.run)
        test.run()

    print("Итеративное вычисление степени")

    power: PowerBase = PowerIter()
    test()

    print("==============================")
    print("Рекурсивное вычисление степени")

    power = PowerRecursion()
    test()
