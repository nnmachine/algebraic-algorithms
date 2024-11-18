from os import path


class TestBase:
    _test_path: list[str]
    _file_name: str

    def __init__(self, run) -> None:
        self._run = run

    def run(self) -> None:
        iter = 0

        while True:
            file_in = path.join(
                *self._test_path,
                f"{self._file_name}.{iter}.in",
            )
            file_out = path.join(
                *self._test_path,
                f"{self._file_name}.{iter}.out",
            )
            if not path.exists(file_in) or not path.exists(file_out):
                return

            with open(file_in, "r") as f:
                in_ = f.read().strip()
            with open(file_out, "r") as f:
                out_ = f.read().strip()

            result = self._run_test(in_)

            if result == out_:
                print(f"Тест {iter} ОК")
            else:
                print(f"Тест {iter} ошибка")

            iter += 1

    def _run_test(self, in_: str) -> str:
        raise NotImplementedError
